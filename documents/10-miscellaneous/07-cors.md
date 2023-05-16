<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
<!-- **Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)* -->

- [<span id="jump-cors"> 跨源资源共享(CORS)</span>](#span-idjump-cors-%E8%B7%A8%E6%BA%90%E8%B5%84%E6%BA%90%E5%85%B1%E4%BA%ABcorsspan)
  - [浏览器的同源策略](#%E6%B5%8F%E8%A7%88%E5%99%A8%E7%9A%84%E5%90%8C%E6%BA%90%E7%AD%96%E7%95%A5)
  - [CORS 预检请求(Preflight request)](#cors-%E9%A2%84%E6%A3%80%E8%AF%B7%E6%B1%82preflight-request)
  - [CORS 若干访问控制场景](#cors-%E8%8B%A5%E5%B9%B2%E8%AE%BF%E9%97%AE%E6%8E%A7%E5%88%B6%E5%9C%BA%E6%99%AF)
  - [常见跨域解决方式](#%E5%B8%B8%E8%A7%81%E8%B7%A8%E5%9F%9F%E8%A7%A3%E5%86%B3%E6%96%B9%E5%BC%8F)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# <span id="jump-cors"> [跨源资源共享(CORS)](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/CORS)</span>

跨源资源共享 (CORS)是一种基于 HTTP 头的机制，该机制 **通过允许服务器标示除了它自己以外的其它 origin（域，协议和端口），使得浏览器允许这些 origin 访问加载自己的资源。** 跨源域资源共享（CORS）机制允许 Web 应用服务器进行跨源访问控制，从而使跨源数据传输得以安全进行。

跨源资源共享还通过一种机制来检查服务器是否会允许要发送的真实请求，_该机制通过浏览器发起一个到服务器托管的跨源资源的 **"预检"请求**_。在预检中，浏览器发送的头中标示有 HTTP 方法和真实请求中会用到的头。

**出于安全性，浏览器限制脚本内发起的跨源 HTTP 请求**。例如，XMLHttpRequest 和 Fetch API 遵循**同源策略**。  
这意味着使用这些 API 的 Web 应用程序只能从加载应用程序的同一个域请求 HTTP 资源，除非响应报文包含了正确 CORS 响应头。

现代浏览器支持在 API 容器中（例如 XMLHttpRequest 或 Fetch）使用 CORS，以降低跨源 HTTP 请求所带来的风险。

CORS 请求失败会产生错误，但是为了安全，在 JavaScript 代码层面是无法获知到底具体是哪里出了问题。你只能查看浏览器的控制台以得知具体是哪里出现了错误。

## [浏览器的同源策略](https://developer.mozilla.org/zh-CN/docs/Web/Security/Same-origin_policy)

**源/起源(origin)** : Web 内容的源由用于访问它的`URL`的方案(协议)scheme(protocol)，主机(域名)hostname(domain)和端口 port 定义。

**同源(same-origin)**: 如果两个`URL`的 protocol、port(如果有指定的话)和 host 都相同的话，则这两个`URL`是同源。

**同源策略(same-origin policy)**: 浏览器的同源策略是一个重要的安全策略，它用于**限制一个源的文档或者它加载的脚本，如何与另一个源的资源进行交互**。它能帮助阻隔恶意文档，减少可能被攻击的媒介。

- **源的继承**: 在页面中通过 `about:blank` 或 `javascript:` URL 执行的脚本*会继承打开该 URL 的文档的源*，
  - 因为这些类型的 URLs 没有包含源服务器的相关信息。
- **IE 中的同源策略的特例**
  - 授信范围（Trust Zones）：_两个相互之间高度互信的域名_，如公司域名（corporate domains），则*不受同源策略限制*。
  - 端口：IE *未将端口号*纳入到同源策略的检查中。
- **源的更改**: 脚本可以将 `document.domain` 的值设置为**其当前域或其当前域的父域**。如果将其设置为其当前域的父域，则这个较短的父域将用于后续源检查。
  - 使用 `document.domain` 来*允许子域安全访问其父域*时，您需要在父域和子域中设置 `document.domain` 为相同的值。
  - 这是必要的，即使这样做只是将父域设置回其原始值。不这样做可能会导致权限错误。

**跨源网络访问**: 同源策略*控制不同源之间的交互*，例如在使用`XMLHttpRequest` 或 `<img>` 标签时则会受到同源策略的约束。通常分为三类：

- 跨源**写操作**(cross-origin writes)**一般是被允许的**。例如链接（links），重定向以及表单提交。_特定少数的 HTTP 请求需要添加预检请求_。
- 跨源**资源嵌入**(cross-origin embedding)**一般是被允许**。
- 跨源**读操作**(cross-origin reads)**一般是不被允许的**，但常可以通过内嵌资源来巧妙的进行读取访问。

**可能嵌入跨源的资源的一些示例**:

- `<script src="..."></script>` 标签嵌入跨源脚本。语法错误信息只能被同源脚本中捕捉到。
- `<link rel="stylesheet" href="...">` 标签嵌入 CSS。
  - 由于 CSS 的松散的语法规则，CSS 的跨源需要一个设置正确的 HTTP 头部 `Content-Type`。不同浏览器有不同的限制。
- 通过 `<img>` 展示的图片。
- 通过 `<video>` 和 `<audio>` 播放的多媒体资源。
- 通过 `<object>`、`<embed>`和 `<applet>` 嵌入的插件。
- 通过 `@font-face` 引入的字体。一些浏览器允许跨源字体（cross-origin fonts），一些需要同源字体（same-origin fonts）。
- 通过 `<iframe>` 载入的**任何资源**。站点可以使用 `X-Frame-Options`消息头来**阻止**这种形式的跨源交互。

**如何允许跨源访问**: 可以使用 CORS 来允许跨源访问。CORS 是 HTTP 的一部分，它允许**服务端来指定**哪些主机可以从这个服务端加载资源。

**如何阻止跨源访问**:

- 阻止跨源**写操作**，只要**检测请求中的一个不可推测的标记** (CSRF token) 即可。
  - 这个标记被称为 Cross-Site Request Forgery (CSRF) 标记。你必须使用这个标记来阻止页面的跨源读操作。
- 阻止资源的**跨源读取**，需要**保证该资源是不可嵌入的**。阻止嵌入行为是必须的，因为嵌入资源通常向其暴露信息。
- 阻止**跨源嵌入**，需要确保你的资源**不能通过以上列出的可嵌入资源格式使用**。浏览器可能不会遵守 `Content-Type` 头部定义的类型。

**跨源脚本 API 访问**

- JS 的 API 中，很多*允许文档间直接相互引用*。当两个文档的*源不同时*，这些引用方式将对 Window 和 Location 对象的访问添加限制。
- 为了能**让不同源中文档进行交流**，可以使用 `window.postMessage`
- _允许以下对 Window 属性的跨源访问_(某些浏览器可能更多)
  - 方法: `window.blur`、`window.close`、`window.focus`、`window.postMessage`
  - 属性(未注明则为只读): `window.closed` 、`window.frames`、`window.length`、`window.location` 读/写、`window.opener`、`window.parent`、`window.self`、`window.top`、`window.window`
- _允许以下对 Location 属性的跨源访问_(某些浏览器可能更多)
  - 方法: `location.replace`。属性: `HTMLAnchorElement.href` 只写。

**跨源数据存储访问**: 访问存储在浏览器中的数据，如 localStorage 和 IndexedDB，是以源进行分割。**每个源都拥有自己单独的存储空间**，一个源中的 JavaScript 脚本**不能**对属于其它源的数据进行读写操作。

- Cookies 使用不同的源定义方式。_一个页面可以为本域和其父域设置 cookie，只要是父域不是公共后缀（public suffix）即可_。
- 不管使用哪个协议（HTTP/HTTPS）或端口号，**浏览器都允许给定的域以及其任何子域名 (sub-domains) 访问 cookie**。
  - 设置 cookie 时，可以使用 `Domain`、`Path`、`Secure`、和 `HttpOnly` 标记来限定其无障碍。
  - 读取 cookie 时，无法知道它是在哪里被设置的。
  - _即使只使用安全的 https 连接，看到的任何 cookie 都有可能是使用不安全的连接进行设置的_。

## [CORS 预检请求(Preflight request)](https://developer.mozilla.org/zh-CN/docs/Glossary/Preflight_request)

一个 CORS 预检请求是**用于检查服务器是否支持 CORS 即跨域资源共享**。它是一个 `OPTIONS` 请求, 使用了 3 个 HTTP 请求头: `Access-Control-Request-Method`, `Access-Control-Request-Headers`, 和 `Origin` header。

(当然，如果是同源的，就不会有 CORS 预检查，不管是不是有自定义请求头)

当有必要的时候，_浏览器会自动发出一个预检请求_；所以在正常情况下，前端开发者不需要自己去发这样的请求。

示例:一个客户端可能会在实际发送一个`DELETE`请求之前，先向服务器发起一个*预检请求*，用于询问是否可以向服务器发起一个 `DELETE` 请求:

```
OPTIONS /resource/foo
Access-Control-Request-Method: DELETE
Access-Control-Request-Headers: origin, x-requested-with
Origin: https://foo.bar.org
```

如果服务器允许，那么服务器就会响应这个预检请求。并且其响应首部 `Access-Control-Allow-Methods` 会将 `DELETE` 包含在其中:

```
HTTP/1.1 200 OK
Content-Length: 0
Connection: keep-alive
Access-Control-Allow-Origin: https://foo.bar.org
Access-Control-Allow-Methods: POST, GET, OPTIONS, DELETE
Access-Control-Max-Age: 86400
```

规范要求，对那些*可能对服务器数据产生副作用的 HTTP 请求方法*（特别是 GET 以外的 HTTP 请求，或者搭配某些 MIME 类型 的 POST 请求），_浏览器必须首先使用 OPTIONS 方法发起一个预检请求_，从而获知服务端是否允许该跨源请求。_服务器确认允许之后，才发起实际的 HTTP 请求。_ 在预检请求的*返回中*，服务器端也可以通知客户端，_是否需要携带身份凭证_（包括 Cookies 和 HTTP 认证相关数据）。

## CORS 若干访问控制场景

需要 CORS 的场景: 由 `XMLHttpRequest` 或 `Fetch APIs` 发起的*跨源 HTTP 请求*;Web 字体 (CSS 中通过 `@font-face` 使用跨源字体资源);WebGL 贴图;使用 `drawImage` 将 `Images/video` 画面绘制到 `canvas`;[来自图像的 CSS 图形(Shapes from images)](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Shapes/Shapes_From_Images)……

以下使用三个场景来解释跨源资源共享机制的工作原理。

**1. 简单请求**

**“简单请求”不会触发 CORS 预检请求。**若请求**满足所有下述条件**，则该请求可视为“简单请求”：

- 使用下列方法之一：`GET`、`HEAD`、`POST`
- 除了被用户代理自动设置的*首部字段，允许人为设置*的字段为 Fetch 规范定义的 对 CORS 安全的首部字段集合，该集合为：
  - `Accept`、`Accept-Language`、`Content-Language`、`Content-Type`
  - `Content-Type` 的值仅限于下列三者之一:
    - `text/plain`、`multipart/form-data`、`application/x-www-form-urlencoded`
- 请求中的任意`XMLHttpRequest`对象**均没有**注册任何事件监听器;
  - `XMLHttpRequest`对象可以用`XMLHttpRequest.upload`属性访问
- 请求中没有使用 `ReadableStream` 对象。

_客户端和服务器之间使用 CORS 首部字段来处理权限._

- 请求首部字段 `Origin` 表明该请求来源
- 服务端返回的 `Access-Control-Allow-Origin:*`表明该资源可以被**任意**外域访问。如果`*`改为网址，表示服务端仅允许该网址访问。
  - 当响应的是附带身份凭证的请求时，服务端**必须**明确 `Access-Control-Allow-Origin` 的值，而不能使用通配符`*`。

**2. 预检请求**

“预检请求”**要求必须首先**使用 `OPTIONS` 方法发起一个预检请求到服务器，以获知服务器是否允许该实际请求。  
_“预检请求”的使用，可以避免跨域请求对服务器的用户数据产生未预期的影响_。

**示例**: 使用 POST 请求发送一个 XML 文档，该请求包含了一个自定义的请求首部字段（`X-PINGOTHER: pingpong`）_就像实际使用的自定义请求头_。另外，该请求的 `Content-Type` 为 `application/xml`。因此，该请求需要首先发起“预检请求”。

```
xhr.setRequestHeader('X-PINGOTHER', 'pingpong');
xhr.setRequestHeader('Content-Type', 'application/xml');
```

首次交互是预检请求/响应:

*浏览器*检测到从 js 中发起的请求需要被预检。发送了一个使用`OPTIONS`方法的“预检请求”。预检请求中同时携带了下面两个首部字段：

```sh
Access-Control-Request-Method: POST # 告知服务器，实际请求将使用 POST 方法
Access-Control-Request-Headers: X-PINGOTHER, Content-Type # 告知服务器，实际请求将携带两个自定义请求首部字段
```

OPTIONS 是 HTTP/1.1 协议中定义的方法，用以从服务器获取更多信息。该方法不会对服务器资源产生影响。

*服务器*将接受后续的实际请求，响应中带有如下信息:

```sh
Access-Control-Allow-Origin:https://foo.example # 限制请求的源域
Access-Control-Allow-Methods:POST, GET, OPTIONS # 表明服务器允许客户端使用 POST 和 GET 方法发起请求
Access-Control-Allow-Headers:X-PINGOTHER,Content-Type #表明服务器允许请求中携带此两个字段
Access-Control-Max-Age:86400 # 表明该响应的有效时间为 86400 秒。在有效时间内浏览器无须为同一请求再次发起预检请求。
```

预检请求完成之后，发送实际请求，服务器返回对应响应。

**预检请求与重定向**: 并不是所有浏览器都支持预检请求的重定向。如果一个预检请求发生了重定向，一部分浏览器将报告错误。  
如果浏览器未实现，规避报错的两种方式: 在服务端去掉对预检请求的重定向；将实际请求变成一个简单请求。  
如果还不行: 先发出一个简单请求以判断真正的预检请求会返回什么地址。再发出另一个请求（真正的请求）。  
如果请求是**由于存在 Authorization 字段而引发了预检请求**，则这一方法将无法使用。这种情况只能由服务端进行更改。

**3. 附带身份凭证的请求**

一般而言，对于跨源 `XMLHttpRequest` 或 `Fetch` 请求，浏览器 **不会** 发送身份凭证信息。如果要发送凭证信息，需要*设置 `XMLHttpRequest` 的某个特殊标志位*。

- 当发出跨源请求时，第三方 cookie 策略仍将适用。无论如何改变以下描述的服务器和客户端的设置，该策略都会强制执行。

示例: `https://foo.example` 的某脚本向 `https://bar.other` 发起一个 GET 请求，并设置 Cookies:

```js
const invocation = new XMLHttpRequest();
const url = "https://bar.other/resources/credentialed-content/";

function callOtherDomain() {
  if (invocation) {
    // 因为这是一个简单 GET 请求，所以浏览器不会对其发起“预检请求”。
    invocation.open("GET", url, true);
    // 将 XMLHttpRequest 的 withCredentials 标志设置为 true，从而向服务器发送 Cookies
    invocation.withCredentials = true;
    invocation.onreadystatechange = handler;
    invocation.send();
  }
}
```

**如果服务器端的响应中未携带 `Access-Control-Allow-Credentials: true`，浏览器将不会把响应内容返回给请求的发送者。**  
注意在 CORS 响应中设置的 cookies ,适用于一般性第三方 cookie 策略。  
强制执行的 cookie 策略可能会使本节描述的内容无效（阻止你发出任何携带凭据的请求）。

CORS 预检请求**不能**包含凭据。预检请求的**响应**必须指定 `Access-Control-Allow-Credentials: true` 来表明*可以携带凭据*进行实际的请求。在响应附带身份凭证的请求时:

- 服务器**不能**将 `Access-Control-Allow-Origin` 的值设为通配符`*`，而应将其设置为特定的域
  - 请求的首部中携带了 `Cookie` 信息，如果 `Access-Control-Allow-Origin` 的值为`*`，请求将会`失败`。
  - 响应首部中也携带了 `Set-Cookie` 字段，尝试对 Cookie 进行修改。如果操作失败，将会抛出异常
- 服务器**不能**将 `Access-Control-Allow-Headers` 的值设为通配符`*`，而应将其设置为首部名称的列表
- 服务器**不能**将 `Access-Control-Allow-Methods` 的值设为通配符`*`，而应将其设置为特定请求方法名称的列表

**规范所定义的响应首部字段(The HTTP response headers)**

```sh
Access-Control-Allow-Origin: <origin> | *  # 指定允许访问该资源的外域 URI。如果服务端指定了具体的域名而非“*”，那么响应首部中的 Vary 字段的值必须包含 Origin。这将告诉客户端：服务器对不同的源站返回不同的内容。
Access-Control-Expose-Headers: X-My-Custom-Header # 让服务器把允许浏览器访问的头放入白名单
Access-Control-Max-Age: xxx # 请求的结果能够被缓存多久。预检请求的结果在xxx秒内有效
Access-Control-Allow-Credentials:true # 浏览器的 credentials 设置为 true 时是否允许浏览器读取 response 的内容
Access-Control-Allow-Methods: <method>[, <method>]* # 指明了实际请求所允许使用的 HTTP 方法。
Access-Control-Allow-Headers: <field-name>[, <field-name>]* # 指明了实际请求中允许携带的首部字段。
```

**可用于发起跨源请求的首部字段(The HTTP request headers)**

这些首部字段无须手动设置。当开发者使用 XMLHttpRequest 对象发起跨源请求时，它们已经被设置就绪

```sh
# 注意，在所有访问控制请求（Access control request）中，Origin 首部字段 总是 被发送。
Origin: <origin> # 表明预检请求或实际请求的源站。origin不包含任何路径信息，只是服务器名称。
Access-Control-Request-Method: <method> # 将实际请求所使用的 HTTP 方法告诉服务器。
Access-Control-Request-Headers: <field-name>[, <field-name>]* # 将实际请求所携带的首部字段告诉服务器。
```

## [常见跨域解决方式](http://www.imooc.com/article/291931)

jsonp: 利用`<script>`标签没有跨域限制，通过`<script>`标签 src 属性，发送带有 callback 参数的 GET 请求，服务端将接口返回数据拼凑到 callback 函数中，返回给浏览器，浏览器解析执行，从而前端拿到 callback 函数返回的数据。

**CORS(跨域资源共享)**: CORS 请求设置的响应头字段(上述所讲，`Access-Control-Allow-Origin: <origin> | *`必选)

**nginx 反向代理实现跨域**: nginx 代理跨域，实质和 CORS 跨域原理一样，通过配置文件设置请求响应头`Access-Control-Allow-Origin`等字段。

**node 中间件代理跨域**: 原理大致与 nginx 相同，都是通过启一个代理服务器，实现数据的转发，也可以通过设置`cookieDomainRewrite`参数修改响应头中 cookie 中域名，实现当前域的 cookie 写入，方便接口登录认证(例如`koa2-cors`中间件)。

_webpack-dev-server_: 配置 webpack 的 devServer 选项

postMessage 解决跨域: postMessage 允许你从一个 iframe 向另一个 iframe 发送 MessageEvent。  
所接收的 page 用`window.addEventListener('message',(receiveMessage)=>{/*do something*/})`来获取到发送页面的消息

websocket 实现跨域: websocket 进行通信不需要考虑跨域的问题,但使用 websocket 进行通信需要保证 websocket 的唯一状态

gateway 服务的全局跨域设置

```java
package com.example.gateway.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.cors.CorsConfiguration;
import org.springframework.web.cors.reactive.CorsWebFilter;
import org.springframework.web.cors.reactive.UrlBasedCorsConfigurationSource;
import org.springframework.web.util.pattern.PathPatternParser;

/* 全局跨域配置类 */
@Configuration
public class CorsConfig {
    private CorsConfiguration buildConfig() {
        CorsConfiguration corsConfiguration = new CorsConfiguration();
        // 允许任何域名使用
        corsConfiguration.addAllowedOrigin("*");
        // 允许任何头
        corsConfiguration.addAllowedHeader("*");
        // 允许任何方法（post、get等）
        corsConfiguration.addAllowedMethod("*");
        corsConfiguration.addExposedHeader("Authorization:");
        corsConfiguration.setAllowCredentials(Boolean.TRUE);
        return corsConfiguration;
    }

    @Bean
    public CorsWebFilter corsFilter() {
        UrlBasedCorsConfigurationSource source = new UrlBasedCorsConfigurationSource(new PathPatternParser());
        // 对接口配置跨域设置
        source.registerCorsConfiguration("/**", buildConfig());
        return new CorsWebFilter(source);
    }
}

```

security 服务的跨域设置

```java
package com.example.security.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

/* 跨域配置 */
@Configuration
public class CrossConfig implements WebMvcConfigurer {
    /** 跨域拦截*/
    @Override
    public void addCorsMappings(CorsRegistry registry) {
        //允许所用请求路径
        registry.addMapping("/**")
                //请求头
                .allowedHeaders("*")
                //请求方法（GET,POST,PUT,DELETE,PATCH）
                .allowedMethods("*")
                //允许所有域名
                .allowedOrigins("*")
                //允许cookie等凭证
                .allowCredentials(true)
                //有效期
                .maxAge(3600);
    }
}
```
