# webpack5 简单配置示例

## 说明

这里只是记录 webpack 配置文件的一些选项的作用和一些功能的示例，直接复制代码去运行不一定行。
具体测试看项目[webpack5-config-demo](https://gitlab.com/looking-for-jobs/webpack5-config-demo)

因为配置代码中对每个配置都有说明，直接看代码注释就好。

webpack 文档官方就有中文[webpack 指南](https://webpack.docschina.org/guides/)

## webpack 常规配置

`webpack.config.part1.js`的配置，则为 webpack 常规的配置，包括压缩、优化、各类加载、插件等。

文件名 `webpack.config.part1.js`:

```js
const path = require("path");
// 由于 webpack 只认识 js，因此需通过 html-webpack-plugin 插件打包 html 文件
const HtmlWebpackPlugin = require("html-webpack-plugin");
// 每次打包都清除之前打包的文件
const { CleanWebpackPlugin } = require("clean-webpack-plugin");
// 分离样式文件的插件
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
// 压缩css的插件
const CssMinimizerPlugin = require("css-minimizer-webpack-plugin");
// 借助插件 webpack-bundle-analyzer 我们可以直观的看到打包结果中，文件的体积大小、各模块依赖关系、文件是够重复等问题
const BundleAnalyzerPlugin =
  require("webpack-bundle-analyzer").BundleAnalyzerPlugin;
// 压缩js，webpack5内置的
const TerserPlugin = require("terser-webpack-plugin");
// purgecss-webpack-plugin 会单独提取 CSS 并清除用不到的 CSS
const PurgecssWebpackPlugin = require("purgecss-webpack-plugin");
const glob = require("glob"); // 文件匹配模式

// 导入 babel 的配置
const babelOptions = require("./babelrc.js");

// 路径处理方法
function resolve(dir) {
  console.log("别名配置resolve后的路径: ", path.join(__dirname, "..", dir));
  return path.join(__dirname, "..", dir);
}

const config = {
  // 模式
  mode: "none",
  // 打包入口地址
  // entry: './src/part2/index.js',
  entry: path.resolve(__dirname, "../src/part2/index.js"),
  output: {
    // 打包输出文件名
    filename: "bundle.[fullhash:8].js",
    // 打包输出文件目录
    // path: path.join(__dirname, 'dist-dev/part2') // __dirname 为当前文件路径
    // 打包输出文件目录
    path: path.resolve("dist-dev/part2"),
  },
  // SourceMap 是一种映射关系，当项目运行后，如果出现错误，我们可以利用 SourceMap 反向定位到源码位置 。打包后js以.map为后缀
  // 除了surce-map外还有很多其他配置，简单的区别参看：
  devtool: "source-map",
  // 配置模块如何解析
  resolve: {
    // 尝试按顺序解析这些后缀名（导入模块时可不加后缀）。
    // 如果有多个文件有相同的名字，但后缀名不同，webpack 会解析列在数组首位的后缀的文件 并跳过其余的后缀。高频文件后缀名放前面.
    extensions: [".js", ".css", ".scss", ".json", ".wasm", "..."],
    // 创建 import 或 require 的别名，来确保模块引入变得更简单。例如
    alias: {
      "@": resolve("src"),
      "~2": resolve("src/part2"),
    },
    // 告诉 webpack 解析模块时应该搜索的目录,优先 src 目录下查找需要解析的文件，会大大节省查找时间
    modules: [resolve("src"), "node_modules"],
  },
  // 配置本地服务
  devServer: {
    static: path.resolve(__dirname, "../public"), // 静态文件目录
    compress: true, //是否启动压缩 gzip
    port: 4200, // 端口号
    // open: true  // 是否自动打开浏览器
  },
  optimization: {
    // tree-shaking的配置
    // https://webpack.docschina.org/guides/tree-shaking/
    // 需要先在package.json中配置: "sideEffects": false // 默认true，表示当前项目中的模块是否有副作用
    // 2022-06-24 根据官网配置了tree-shaking，但未使用的js代码，还是打包到bundle中去了。例如math.js的square()方法，没有用到，但打包了
    sideEffects: true, // 默认false，表示是否移除无副作用的模块
    // sideEffects 和 usedExports（更多被认为是 tree shaking）是两种不同的优化方式.
    // sideEffects 更为有效 是因为它允许跳过整个模块/文件和整个文件子树。
    usedExports: true,
    // 开发环境也最小压缩
    // minimize: true,
    minimizer: [
      // For webpack@5 you can use the `...` syntax to extend existing minimizers
      // (i.e. `terser-webpack-plugin`), uncomment the next line
      // `...`,
      // css的最小压缩插件
      new CssMinimizerPlugin(),
      // webpack5 内置js最小压缩插件
      new TerserPlugin({}),
    ],
  },
  // 配置资源加载模块
  module: {
    rules: [
      // 转换规则
      {
        //匹配所有的 sass/scss/css 文件
        test: /\.(s[ac]|c)ss$/i,
        // use: 对应的 Loader. 名称 Loader 就是将 Webpack 不认识的内容转化为认识的内容
        // Loader 的执行顺序是固定【从后往前】，即按 css-loader --> style-loader 的顺序执行
        use: [
          // 'style-loader',   // style-loader 就是将处理好的 css 通过 style 标签的形式添加到页面上
          // 分离样式文件，通过 CSS 文件的形式引入到页面上（可以在浏览器elements中查看与使用style-loader引入样式的区别）
          MiniCssExtractPlugin.loader,
          "css-loader",
          "postcss-loader", // 使用 postcss-loader，自动添加 CSS3 部分属性的浏览器前缀（未成功）
          "sass-loader", // Sass 不光需要安装 sass-loader 还得搭配一个 node-sass
        ],
      },
      /*
            // 2022-06-24 webpack5 已经不推荐使用file-loader，打包css的背景图会找不到，参看：
            // https://blog.csdn.net/qq_45770253/article/details/123862085
            {
                // 匹配图片文件
                test: /\.(jpe?g|png|gif)$/i,
                use: [

                    {
                        // 使用 file-loader
                        loader: 'file-loader',
                        options: {
                            name: '[name].[hash:8].[ext]',
                            // 文件小于 50k 会转换为 base64，大于则拷贝文件
                            limit: 50 * 1024,
                            esModule: false
                        }
                    },
                ],
                type: 'javascript/auto'
            },
            */
      // webpack5 使用新的方式代替
      {
        test: /\.(jpe?g|png|gif)$/i,
        type: "asset/resource",
        // 打包的图片文件名
        generator: {
          filename: "[name].[hash:8].[ext]",
        },
        // 小于 50kb 的文件，将会视为 inline 模块类型，否则会被视为 resource 模块类型。(不设，默认为8kb)
        parser: {
          dataUrlCondition: {
            maxSize: 50 * 1024,
          },
        },
      },
      // 使用 babel 打包js，配置将 ES6 语法转化为 ES5 等，使得浏览器兼容等
      // 先安装 npm install babel-loader @babel/core @babel/preset-env -D
      // babel-loader 使用 Babel 加载 ES2015+ 代码并将其转换为 ES5
      // @babel/core Babel 编译的核心包
      // @babel/preset-env Babel 编译的预设，可以理解为 Babel 插件的超集
      // 默认配置（建议拆出来避免太臃肿，例如根目录的babelrc.js）
      {
        test: /\.js$/i,
        use: [
          {
            // 开启多进程打包
            loader: "thread-loader",
            // 有同样配置的 loader 会共享一个 worker 池
            options: {
              // 产生的 worker 的数量，默认是 (cpu 核心数 - 1)，或者，
              // 在 require('os').cpus() 是 undefined 时回退至 1
              workers: 3,
              // 一个 worker 进程中并行执行工作的数量
              // 默认为 20
              workerParallelJobs: 50,
              // 额外的 node.js 参数
              workerNodeArgs: ["--max-old-space-size=1024"],
              // 允许重新生成一个僵死的 work 池
              // 这个过程会降低整体编译速度
              // 并且开发环境应该设置为 false
              poolRespawn: false,
              // 闲置时定时删除 worker 进程
              // 默认为 500（ms）
              // 可以设置为无穷大，这样在监视模式(--watch)下可以保持 worker 持续存在
              poolTimeout: 2000,
              // 池分配给 worker 的工作数量
              // 默认为 200
              // 降低这个数值会降低总体的效率，但是会提升工作分布更均一
              poolParallelJobs: 50,
              // 池的名称
              // 可以修改名称来创建其余选项都一样的池
              name: "my-pool",
            },
          },
          // babel的打包配置
          {
            loader: "babel-loader",
            options: babelOptions,
          },
        ],
      },
    ],
  },
  // 与 Loader 用于转换特定类型的文件不同，插件（Plugin）可以贯穿 Webpack 打包的生命周期，执行不同的任务
  plugins: [
    // 配置插件
    // 打包html的插件
    new HtmlWebpackPlugin({
      // html 模板文件的相对/绝对路径。如果不指定模板 template 配置，将是插件默认的 html文件，而不是项目中的 html 文件
      template: "./src/part2/index.html",
      // 打包后的文件名
      filename: "index.html",
      // 压缩配置
      minify: {
        // 删除属性双引号
        removeAttributeQuotes: true,
        // 代码压缩成一行
        // collapseWhitespace: true
      },
      // 引入文件带上hash戳
      hash: true,
    }),
    // 引入每次清空上次打包文件的插件
    new CleanWebpackPlugin(),
    // 分离样式文件的插件
    new MiniCssExtractPlugin({
      filename: "[name].[fullhash:8].css",
    }),
    // 配置构建结果分析插件 （有修改对应的package.json的启动配置）
    new BundleAnalyzerPlugin({
      analyzerMode: "disabled", // 不启动展示打包报告的http服务器
      generateStatsFile: true, // 是否生成stats.json文件
    }),
    // 单独提取 CSS 并清除用不到的 CSS 的插件。没有这个插件，没有使用的class还会保留
    new PurgecssWebpackPlugin({
      paths: glob.sync(`${resolve("src")}/**/*`, { nodir: true }),
    }),
  ],
};

module.exports = (env, argv) => {
  // 使用 cross-env，在package.json中配置好命令，在此处获取环境变量
  console.log("process.env.NODE_ENV=", process.env.NODE_ENV); // 打印环境变量

  console.log("argv.mode=", argv.mode); // 打印 mode(模式) 值

  console.log("config", config.entry);

  // 这里可以通过不同的模式修改 config 配置
  return config;
};
```

文件名`postcss.config.js`:

```js
// 使用 postcss-loader，自动添加 CSS3 部分属性的浏览器前缀，对应配置文件
// 要安装： npm install postcss postcss-loader postcss-preset-env -D

module.exports = {
  // plugins: [require("autoprefixer")]
  plugins: [require("postcss-preset-env")],
};
```

文件名`.browserslistrc`:

```
## postcss.config.js 中 postcss-preset-env 的配置文件
; 2022-06-24 配置了没有像教程一样加上浏览器前缀啊？？

# 换行相当于 and
last 2 versions # 回退两个浏览器版本
> 0.5% # 全球超过0.5%人使用的浏览器，可以通过 caniuse.com 查看不同浏览器不同版本占有率
IE 10 # 兼容IE 10
```

文件名`babelrc.js`:

```js
module.exports = {
  // 解决警告：Though the "loose" option was set to "false" in your @babel/preset-env config, it will not be used for @babel/plugin-proposal-private-methods since the "loose" mode option was set to "true" for @babel/plugin-proposal-private-property-in-object.
  // 参考：https://github.com/rails/webpacker/issues/3008 adamransom 的回复
  assumptions: {
    privateFieldsAsProperties: true,
  },
  cacheDirectory: true, // 启用缓存
  presets: [
    [
      "@babel/preset-env",
      {
        // useBuiltIns: false 默认值，无视浏览器兼容配置，引入所有 polyfill
        // useBuiltIns: entry 根据配置的浏览器兼容，引入浏览器不兼容的 polyfill
        // useBuiltIns: usage 会根据配置的浏览器兼容，以及你代码中用到的 API 来进行 polyfill，实现了按需添加
        useBuiltIns: "entry",
        corejs: "3.9.1", // 是 core-js 版本号
        targets: {
          chrome: "58",
          ie: "11",
        },
      },
    ],
  ],
  // babel的插件，例如打包装饰器等还没有进入规范的提案
  plugins: [
    ["@babel/plugin-proposal-decorators", { legacy: true }],
    ["@babel/plugin-proposal-class-properties"],
  ],
};
```

## webpack devServer 配置

`webpack.config.part2.js`的配置，主要用于测试 webpack 的 devServer 配置，例如代理、mock 请求返回等。

文件名`webpack.config.part2.js`:

```js
let path = require("path");

module.exports = {
  // mode - 打包模式 ： development 为开发模式，打包后代码不会被压缩；production 为生产模式，打包后代码为压缩代码
  mode: "development",
  // 入口文件，指示webpack应该使用哪个模块来开始构建其内部依赖图。webpack 将找出入口点依赖的其他模块和库（直接和间接）。
  entry: {
    app: "./src/part1/index.js",
  },
  // webpack-dev-server 配置
  // webpack-dev-server可用于快速开发应用程序,在4.0版本之后，会直接把static配置的静态资源文件目录下项目进行部署
  devServer: {
    static: path.resolve(__dirname, "../src/part1/"), // 静态文件目录
    // 端口号
    port: 5000,
    // 开启 gzip 压缩
    compress: true,
    // 启动后自动把页面打开
    // open: true,
    // 在浏览器中以百分比显示编译进度
    client: { progress: true },
    // 使用代理配置解决接口跨域问题

    proxy: {
      // 检测到请求路径中有 baike 关键字，会替换目标请求地址为target，并将请求中的 baike 替换为 api/openapi/BaikeLemmaCardApi
      "/baike": {
        // 接口域名
        target: "http://baike.baidu.com",
        // 接口路径重写，把请求代理到接口服务器上
        pathRewrite: { baike: "api/openapi/BaikeLemmaCardApi" },
        // 默认情况下，将不接受在 HTTPS 上运行且证书无效的后端服务器。 如果需要，可以这样修改配置
        secure: false,
        // 修改跨域
        changeOrigin: true,
      },
    },

    // 通过 mock 前端跟后端约定好的接口数据格式来模拟调试页面。
    // 可使用有自定义函数和应用自定义中间件的能力的配置 devServer.setupMiddlewares，
    // 在 middlewares.unshift 中的回调函数使用 res.send 把需要 mock 的数据传递进去：
    setupMiddlewares: (middlewares, devServer) => {
      if (!devServer) {
        throw new Error("webpack-dev-server is not defined");
      }

      middlewares.unshift({
        // name和path可以不一样。path是地址，name只是该地址的名称
        name: "user-info",
        // `path` 是可选的，接口路径
        path: "/user",
        middleware: (req, res) => {
          // mock 数据模拟接口数据
          res.send({ name: "user data mock" });
        },
      });

      return middlewares;
    },
  },
};
```

文件名称`index.html`:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Page Title</title>
    <style type="text/css">
      /* 此处要注意.css文件的路径 */
      @import "main.css";
    </style>
  </head>

  <body>
    <h1>This is a Heading</h1>
    <p>This is a paragraph.</p>

    <script src="./index.js"></script>
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
    <script>
      (function () {
        /**
         * 使用axios请求，测试 webpack.devServer的一些配置
         * */

        // 这里请求的地址是：http://localhost:5000/user，
        // 在webpack.config.js中配置的devServer.setupMiddlewares中的middlewares.unshift有mock该path的请求返回数据
        // 那么这里可以获取该mock数据
        axios
          .get("/user")
          .then(function (response) {
            // handle success
            console.log(response);
          })
          .catch(function (error) {
            // handle error
            console.log(error);
          })
          .then(function () {
            // always executed
          });

        // 这里请求的地址是：http://localhost:5000/baike?scope=103&format=json&appid=379020&bk_key=hero&bk_length=600
        // 但因为在webpack.config.js中配置的devServer.proxy中有配置路劲中含 baike 的代理
        // 所以实际请求的地址会替换为：http://baike.baidu.com/api/openapi/BaikeLemmaCardApi?scope=103&format=json&appid=379020&bk_key=hero&bk_length=600
        // 但在浏览器中的network看到的还是前者的地址，代理后的实际地址是看不到的
        axios
          .get(
            "/baike?scope=103&format=json&appid=379020&bk_key=hero&bk_length=600"
          )
          .then(function (response) {
            // handle success
            console.log(response);
          })
          .catch(function (error) {
            // handle error
            console.log(error);
          })
          .then(function () {
            // always executed
          });

        // 这个请求为 http://localhost:5000/notdemo，它没有配置mock，也没有代理，所以就会是404 Not Found
        axios
          .get("/notdemo")
          .then(function (response) {
            // handle success
            console.log(response);
          })
          .catch(function (error) {
            // handle error
            console.log(error);
          })
          .then(function () {
            // always executed
          });
      })();
    </script>
  </body>
</html>
```

## 其他补充

### [sourceMap 的 devtool 配置的比较](https://juejin.cn/post/7023242274876162084#heading-20)

| devtool                      | build | rebuild       | 显示代码 | SourceMap 文件 | 描述         |
| ---------------------------- | ----- | ------------- | -------- | -------------- | ------------ |
| (none)                       | 很快  | 很快          | 无       | 无             | 无法定位错误 |
| eval                         | 快    | 很快（cache） | 编译后   | 无             | 定位到文件   |
| source-map                   | 很慢  | 很慢          | 源代码   | 有             | 定位到行列   |
| eval-source-map              | 很慢  | 一般（cache） | 编译后   | 有（dataUrl）  | 定位到行列   |
| eval-cheap-source-map        | 一般  | 快（cache）   | 编译后   | 有（dataUrl）  | 定位到行     |
| eval-cheap-module-source-map | 慢    | 快（cache）   | 源代码   | 有（dataUrl）  | 定位到行     |
| inline-source-map            | 很慢  | 很慢          | 源代码   | 有（dataUrl）  | 定位到行列   |
| hidden-source-map            | 很慢  | 很慢          | 源代码   | 有             | 无法定位错误 |
| nosource-source-map          | 很慢  | 很慢          | 源代码   | 无             | 定位到文件   |

本地开发推荐：eval-cheap-module-source-map

生产环境推荐：(none) (别人看不到源码)

### ref

https://webpack.docschina.org/guides/  
https://juejin.cn/post/7023242274876162084  
https://blog.csdn.net/qq_14993375/article/details/113838340
