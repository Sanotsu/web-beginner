<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
<!-- **Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)* -->

- [web 安全](#web-%E5%AE%89%E5%85%A8)
  - [安全基础知识](#%E5%AE%89%E5%85%A8%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86)
  - [http 安全和安全标头快速参考](#http-%E5%AE%89%E5%85%A8%E5%92%8C%E5%AE%89%E5%85%A8%E6%A0%87%E5%A4%B4%E5%BF%AB%E9%80%9F%E5%8F%82%E8%80%83)
  - [HTTPS 进行安全连接](#https-%E8%BF%9B%E8%A1%8C%E5%AE%89%E5%85%A8%E8%BF%9E%E6%8E%A5)
  - [防止信息泄露](#%E9%98%B2%E6%AD%A2%E4%BF%A1%E6%81%AF%E6%B3%84%E9%9C%B2)
  - [保护网站免受 XSS 攻击](#%E4%BF%9D%E6%8A%A4%E7%BD%91%E7%AB%99%E5%85%8D%E5%8F%97-xss-%E6%94%BB%E5%87%BB)
  - [保护用户免受跟踪](#%E4%BF%9D%E6%8A%A4%E7%94%A8%E6%88%B7%E5%85%8D%E5%8F%97%E8%B7%9F%E8%B8%AA)
  - [MDN 的 web 安全概述](#mdn-%E7%9A%84-web-%E5%AE%89%E5%85%A8%E6%A6%82%E8%BF%B0)
  - [常见的 web 攻击方式](#%E5%B8%B8%E8%A7%81%E7%9A%84-web-%E6%94%BB%E5%87%BB%E6%96%B9%E5%BC%8F)
    - [XSS](#xss)
    - [CSRF](#csrf)
    - [由 CORS 配置问题引起的漏洞](#%E7%94%B1-cors-%E9%85%8D%E7%BD%AE%E9%97%AE%E9%A2%98%E5%BC%95%E8%B5%B7%E7%9A%84%E6%BC%8F%E6%B4%9E)
    - [Clickjacking](#clickjacking)
    - [基于 DOM 的漏洞](#%E5%9F%BA%E4%BA%8E-dom-%E7%9A%84%E6%BC%8F%E6%B4%9E)
    - [WebSockets 安全漏洞](#websockets-%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E)
    - [SQLi(SQL 注入)](#sqlisql-%E6%B3%A8%E5%85%A5)
    - [OS 命令注入攻击](#os-%E5%91%BD%E4%BB%A4%E6%B3%A8%E5%85%A5%E6%94%BB%E5%87%BB)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# web 安全

## 安全基础知识

**bug**: 在软件开发中，当一个应用程序不能按照预期的方式工作时，它被称为 "bug"。有时，一个 bug 会显示错误的信息或在某个动作上崩溃。

**vulnerability**（漏洞，有时称为 security bug）是一种可能被用于滥用的 bug。

Most security techniques are just good programming:

- 检查用户输入的值(不能是空，不能是 null,检查数据量)- 确保单个用户不会占用太多时间。- 构建单元测试，这样安全漏洞就不会意外出现。

**security features**(安全特性):第一道防线是安全特性，例如 HTTPS、CORS。使用 HTTPS 加密数据可能无法修复错误，但它可以保护您与用户交换给其他方的数据。

**impact**: 当应用不安全(not secure)，在各个方面都有可能造成影响:

- 对于用户: **敏感信息**例如个人数据可能会**泄露或者盗取**。**内容可能被篡改**，被篡改的站点可能会将用户引导至恶意站点。
- 对于应用: 可能会**丢失用户信任**。**业务**可能因由于篡改或系统短缺导致的停机或丧失信心而受到**损失**。
- 对于其他系统: 被劫持的应用程序可用于**攻击其他系统**，例如使用僵尸网络进行拒绝服务攻击(denial-of-service attack,DoS attack)。
  - DoS 攻击: 使目标电脑的网路或系统资源耗尽，使服务暂时中断或停止，导致其正常使用者无法存取。

**attack**: 当恶意方利用漏洞或缺乏安全功能对其有利时造成损害，称为`攻击`。可以分为*主动攻击*与*被动攻击*两种。

- 主动攻击(active attacks):
  - 攻击者试图**直接侵入应用程序**。从使用虚假身份访问敏感数据（伪装攻击,masquerade attack）到用大量流量淹没您的服务器以使您的应用程序无响应（拒绝服务攻击,DoS attack）。
  - 对**传输中的数据**进行主动攻击。攻击者可能会在您的应用程序数据到达用户浏览器之前对其进行修改，从而在站点上显示修改后的信息或将用户引导至意外目的地。这有时称为*消息修改*(modification of messages)。(一个网站被攻击者篡改，引导用户进入钓鱼网站)
- 被动攻击(passive attack):
  - 攻击者试图*从应用程序收集或学习信息，但不影响应用程序本身*。攻击者可以在浏览器和服务器之间捕获数据，收集用户名和密码、用户的浏览历史和交换的数据。

**防御攻击**: 攻击者可以直接损害应用程序或在站点上执行恶意操作，而您或您的用户不会注意到它。您*需要检测和防御攻击的机制。*

没有单一的解决方案可以让应用程序 100% 安全。在实践中，许多*安全特性*和技术被*分层使用*以防止或进一步延迟攻击(这称为**深度防御**)。  
例如应用包含一个表单，可能会检查浏览器中的输入，然后是服务器，最后是数据库；还可以使用 HTTPS 来保护传输中的数据。

**“同站”和“同源”**("same-site" and "same-origin")

**源 (Origin)**: _协议(或者称方案 schema)、主机名和端口（如果指定）的组合_。组合都相同的网站视为 **“同源”**，否则视为 **“跨源”**。

**顶级域 (TLD)**，例如 `.com` 和 `.org` 列在[根区数据库](https://www.iana.org/domains/root/db)中。

**有效顶级域(eTLD)**: 对于 `.co.jp` 或 `.github.io` 等域，仅使用 `.jp` 或 `.io` 的 TLD 不足以识别“站点”。同时，无法通过算法确定特定 TLD 的可注册域的级别。这就是创建“有效 TLD”(eTLD) 列表的原因。  
这些域在[公共后缀列表](https://wiki.mozilla.org/Public_Suffix_List)中进行定义。eTLD 列表的维护网站是 [publicsuffix.org/list](https://publicsuffix.org/list/)。

**完整站点名称**为`eTLD+1`: **有效顶级域加上它前面的域部分。**`eTLD+1`相同的网站被视为 **“同站”**。`eTLD+1`不同的网站则被视为 **“跨站”**。

“同站”的定义正在演变为*将`URL`方案视为站点的一部分*，从而防止将 HTTP 用作[弱通道](https://datatracker.ietf.org/doc/html/draft-west-cookie-incrementalism-01#page-8)。**“有方案同站”**(Schemeful Same-Site)即要求*方案也匹配*的“同站”。

Chrome 将请求与`Sec-Fetch-Site`HTTP 标头一起发送，可以根据该头的值确定请求是“同站”、“同源”还是“跨站”(无法检查有方案的同站)。  
`Sec-Fetch-Site`的值可选项为 `cross-site`、`same-site`、`same-origin`、`none`

## [http 安全](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/CSP)和[安全标头快速参考](https://web.dev/security-headers/)

**1. 常见的安全威胁和应对策略**

[web-security](https://portswigger.net/web-security/all-materials)中可以学习到很多 web 安全方面的东西，比如常见的安全威胁以及应对措施。

**保护网站免受注入漏洞(injection vulnerabilities)的影响**

- 当应用程序处理的*不受信任的数据*会影响其行为并且通常会导致执行攻击者控制的脚本时，就会出现**注入漏洞**。
- 由**注入错误**引起的最常见漏洞是各种形式的**跨站点脚本(XSS)**，包括反射型 XSS、存储型 XSS、基于 DOM 的 XSS 和其他变体。
  - XSS 漏洞通常可以*让攻击者完全访问应用程序处理的用户数据以及托管在同一 Web 源中的任何其他信息*。
- **传统防御措施**: 使用自动转义 HTML 模板系统、避免使用危险的 JavaScript API，以及通过在单独的域中托管文件上传和清理用户控制的 HTML 来正确处理用户数据。
  - 使用`Content Security Policy (CSP)`来控制应用程序可以执行哪些脚本以降低注入风险。
  - 使用`Trusted Types`强制对传递到危险 JavaScript API 的数据进行清理。
  - 使用`X-Content-Type-Options` 防止浏览器误解网站资源的 MIME 类型，从而导致脚本执行。

**将网站与其他网站隔离**(破坏 Web 隔离的问题)

- Web 的开放性允许网站以可能违反应用程序安全预期的方式相互交互。这包括*意外发出经过身份验证的请求或将来自另一个应用程序的数据嵌入攻击者的文档中，从而允许攻击者修改或读取应用程序数据。*
- **破坏 Web 隔离**的常见漏洞包括**点击劫持**、**跨站请求伪造(CSRF)**、**跨站脚本包含(XSSI)** 和各种**跨站泄漏**。
- 保护措施包含:
  - 使用`X-Frame-Options`防止文档被恶意网站嵌入。
  - 使用`Cross-Origin Resource Policy (CORP)`防止网站的资源被跨域网站包含。
  - 使用`Cross-Origin Opener Policy (COOP)`保护网站的窗口免受恶意网站的交互。
  - 使用`Cross-Origin Resource Sharing (CORS)`来控制跨域文档对网站资源的访问。

**安全地建立一个强大的网站**(使用跨域隔离功能)

- 尽管有同源政策，[Spectre(一种安全漏洞)](<https://en.wikipedia.org/wiki/Spectre_(security_vulnerability)>) 还是将任何加载到同一 browsing context group 的数据置于潜在的可读状态。
  - 浏览器限制了可能利用该漏洞的功能，这些功能在一个特殊的环境中被称为"跨源隔离"。
  - 通过跨源隔离，你可以使用诸如 `SharedArrayBuffer` 之类的强大功能。
- **使用`Cross-Origin Embedder Policy (COEP)`和`COOP`来启用跨域隔离**。

**加密到网站的流量**(传输数据加密)

- 当应用程序**未完全加密传输中的数据**时，就会出现加密问题，从而使窃听攻击者能够了解用户与应用程序的交互。
- 可能会出现加密不足的情况: 不使用`HTTPS`、混合内容、设置没有`Secure`属性(或`__Secure`前缀)的 cookie 或松散的`CORS`验证逻辑。
- 应对措施: **使用 `HTTP Strict Transport Security (HSTS)`通过 HTTPS 始终如一地提供您的内容**。

**2. 重要的安全标头说明**

**[Content-Security-Policy CSP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy)**

- 内容安全策略（CSP）用于检测和减轻用于 Web 站点的特定类型的攻击，例如 XSS 和数据注入等。
  - 该安全策略的实现基于一个称作 `Content-Security-Policy` 的 HTTP 首部。
- 配置网络服务器返回 [`Content-Security-Policy`](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Headers/Content-Security-Policy) HTTP 头部(有配置则在 response headers 中可见)。常见策略:

  - _所有内容均来自站点的同一个源_(不包括其子域名):
    - `Content-Security-Policy: default-src 'self'`
  - 允许*内容来自信任的域名及其子域名*(域名不必须与 CSP 设置所在的域名相同):
    - `Content-Security-Policy: default-src 'self' example.com *.example.com`
  - 允许网页应用的*用户在他们自己的内容中包含来自任何源的图片*，但是*限制音频或视频*需从信任的资源提供者 (获得)，*所有脚*本必须从特定主机服务器获取可信的代码。

  ```sh
  Content-Security-Policy: default-src 'self'; img-src *; media-src example.org example.net; script-src userscripts.example.com
  # 图片来源任何站点，媒体只允许来自example.org example.net，可执行脚本只允许来自userscripts.example.com
  ```

  - 确保网站的*所有内容都要通过 SSL 方式获取*，以避免攻击者窃听用户发出的请求。

  ```sh
  Content-Security-Policy: default-src https://onlinebanking.jumbobank.com
  # 该服务器仅允许通过 HTTPS 方式并仅从onlinebanking.jumbobank.com域名来访问文档。
  ```

  - 允许在邮件里包含 HTML，同样图片允许从任何地方加载，但不允许 JavaScript 或者其他潜在的危险内容 (从任意位置加载)。

  ```sh
  Content-Security-Policy: default-src 'self' *.mailsite.com; img-src *
  # 并未指定script-src，站点通过 default-src 指令的对其进行配置，这也同样意味着脚本文件仅允许从原始服务器获取。
  ```

`DOM-based XSS`是一种攻击，即*恶意数据被传入支持动态代码执行的 sink(接收器)*，如`eval()`或`.innerHTML`。

**`Trusted Types`**(现代浏览器支持) 提供了*编写、安全审查和维护不受 DOM XSS 影响的应用程序的工具*。可以通过 CSP 启用，并通过将危险的 Web API 限制为仅接受特殊对象（受信任类型）来使 JavaScript 代码默认安全。

对危险的 DOM 接收器实施可信类型标头配置:

```sh
Content-Security-Policy: require-trusted-types-for 'script'
# 值目前只有script:不允许将字符串与 DOM XSS 注入接收器函数一起使用，并且需要匹配由受信任类型策略创建的类型。
```

如果浏览器支持`window.trustedTypes`，可以在使用 eval()等需要注入 DOM 的地方进行自定字符串替换等策略。

```js
// 检查浏览器是否支持该功能
if (window.trustedTypes && trustedTypes.createPolicy) {
  // 命名并创建一个 policy
  const policy = trustedTypes.createPolicy("escapePolicy", {
    createHTML: (str) => str.replace(/\</g, "&lt;").replace(/>/g, "&gt;");
  });
}
// 应用策略时：原始字符串的分配被Trusted Types所阻止。
el.innerHTML = "some string"; // This throws an exception.
// 信任类型策略的分配被安全地接受。
const escaped = policy.createHTML("<img src=x onerror=alert(1)>");
el.innerHTML = escaped; // '&lt;img src=x onerror=alert(1)&gt;'
```

**[X-Content-Type-Options](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Content-Type-Options)**

当一个恶意的 HTML 文档从你的域中提供时（例如，如果上传至照片服务的图片包含有效的 HTML 标记），一些浏览器会将其视为一个活动文档，并允许其在应用程序的上下文中执行脚本，从而导致**跨站脚本错误**。

`X-Content-Type-Options:nosniff` HTTP 消息头相当于一个提示标志，被服务器用来提示**客户端一定要遵循在`Content-Type`首部中对 MIME 类型的设定，而不能对其进行修改**。这就*禁用了客户端的 MIME 类型嗅探行为*，也就是意味着*网站管理员确定自己的设置没有问题*。

注意：nosniff 只应用于 "script" 和 "style" 两种类型。事实证明，将其应用于图片类型的文件会导致与现有的站点冲突。  
如果请求类型是`style`而 MIME 类型不是`text/css`，或者是请求类型是`script`而 MIME 类型不是[JavaScript MIME 类型](https://html.spec.whatwg.org/multipage/scripting.html#javascript-mime-type)，则阻止请求。

示例: `X-Content-Type-Options: nosniff (换行) Content-Type: text/html; charset=utf-8`

**[X-Frame-Options](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options)**

`X-Frame-Options` HTTP 响应头是用来**给浏览器指示允许一个页面可否在 `<frame>`、`<iframe>`、`<embed>` 或者 `<object>` 中展现的标记**。站点可以通过确保网站没有被嵌入到别人的站点里面，从而**避免点击劫持攻击**(需要浏览器支持该头)。该响应头有两个值:

```sh
X-Frame-Options: DENY # 表示该页面不允许在 frame 中展示，即便是在相同域名的页面中嵌套也不允许。
X-Frame-Options: SAMEORIGIN # 表示该页面可以在相同域名页面的 frame 中展示
```

**[Cross-Origin-Resource-Policy (CORP)(慎用)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cross-Origin-Resource-Policy)**

攻击者的网站可以在弹出的窗口中打开另一个网站，通过利用基于网络的跨站泄漏来了解其信息。在某些情况下，这也可能允许利用基于 Spectre 的侧面通道(side-channel)攻击。

该响应头会**指示浏览器阻止对指定资源的无源跨域/跨站点请求。**

`Cross-Origin-Resource-Policy: same-site | same-origin | cross-origin`，所有资源应该使用其中之一:

- `cross-origin`建议被用于**类似 CDN 的服务资源**，除非它们已经通过 CORS 提供了类似的效果。
- `same-origin` 应该被用于**只由同源页面加载的资源**。你应该把它应用于包含用户敏感信息的资源，或只由同一来源调用的 API 的响应。
- `same-site`建议被用于与上述类似的资源，但要由你网站的**其他子域加载**。

**[Cross-Origin-Opener-Policy (COOP)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cross-Origin-Opener-Policy)**

该响应头允许**确保顶级(top-level)文档不与跨域文档共享浏览上下文组(a browsing context group)。**

**浏览上下文组是一组共享相同上下文的选项卡、窗口或 iframe。**例如，如果网站 (https://a.example) 打开一个弹出窗口 (https://b.example)，打开程序窗口和弹出窗口共享相同的浏览上下文，并且它们可以通过 DOM API (`window.opener`) 相互进行访问。

`Cross-Origin-Opener-Policy`头为文档提供了一种方法，  
使其与通过`window.open()`或不含 `rel="noopener"`的`target="_blank"`链接打开的跨源窗口隔离。因此，*该文档的任何跨源打开者将没有对它的引用，也不能与它进行交互。*他们将无法访问您的全局对象，从而防止了一组称为 `XS-Leaks` 的跨域攻击。

该标头的可选属性为以下:

- `unsafe-none`:这是默认值。_允许将文档添加到其开启者的浏览上下文组_，除非值被设置为以下两个。(允许跨域窗口引用文档)
- `same-origin-allow-popups`:保留对新打开的窗口或标签的引用。(将文档与跨域窗口隔离，但允许弹出窗口)
- `same-origin`:将*浏览上下文专门隔离到同源文档*。跨域文档不会加载到相同的浏览上下文中。(从跨域窗口中隔离文档)

报告模式与 COOP 不兼容，当 COOP 阻止与 Reporting API 的跨窗口交互时，您可以接收报告:  
`Cross-Origin-Opener-Policy: same-origin; report-to="coop"`

**【Cross-Origin Resource Sharing】**参看[跨域资源共享 (CORS)](#jump-cors)

**[Cross-Origin-Embedder-Policy (COEP)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cross-Origin-Embedder-Policy)**

该响应标头可**防止文档加载未明确授予文档权限 (通过 CORP 或者 CORS) 的任何跨域资源。**

```
Cross-Origin-Embedder-Policy: unsafe-none | require-corp
```

- `unsafe-none`:这是默认值。允许文档获取跨源资源，而无需通过 CORS 协议或 `Cross-Origin-Resource-Policy` 头。
- `require-corp`:文档**只能从相同的源**加载资源，或**显式标记为可从另一个源**加载的资源。
  - 如果跨源资源支持`CORS`,则[crossorigin](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Attributes/crossorigin)属性或`Cross-Origin-Resource-Policy`头必须使用它来加载资源而不会被`COEP`阻止。

通过与 COOP 一起发送来启用[跨域隔离(cross-origin isolated)](https://web.dev/coop-coep/):

```SH
Cross-Origin-Embedder-Policy: require-corp
Cross-Origin-Opener-Policy: same-origin
```

**HTTP [Strict-Transport-Security (HSTS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security)**

该响应标头用来通知**浏览器应该只通过 HTTPS 访问该站点**，并且以后*使用 HTTP 访问该站点的所有尝试都应自动转换为 HTTPS*。

```
Strict-Transport-Security: max-age=<expire-time>; includeSubDomains
```

- `max-age=<expire-time>`:设置在**浏览器收到这个请求后的指定秒**的时间内**凡是访问这个域名下的请求都使用 HTTPS 请求**。
- `includeSubDomains` (可选):如果这个可选的参数被指定，那么说明此规则也**适用于该网站的所有子域名**。
- `preload` (可选): 查看 预加载 HSTS 获得详情。不是标准的一部分。
  - 谷歌维护着一个 [HSTS 预加载服务](https://hstspreload.org/)。按照其指示成功提交域名后，浏览器将会**永不使用非安全**的方式连接到你的域名。

**开发环境使用 https 的情况**

- 在使用`Set-Cookie`响应头时设置了选项为`Secure`、`SameSite:none`或者`__Host`的 cookie。
  - `Secure`选项只能用于 https，`SameSite:none`和`__Host`需要 cookie 是`Secure`
- 需要在本地调试一个**只出现在 HTTPS 网站**上而不会出现在 HTTP 网站上的问题(例如混合内容)。
- 需要在本地测试或重现**特定于 HTTP/2 或更高版本的行为**(比如测试 http2 的加载性能)。
- 需要在本地测试需要 **HTTPS 的第三方库或 API**（例如 OAuth）。
- 使用的不是 localhost，而是用于本地开发的**自定义主机名**(修改了本机 host 文件)

**开发环境(本地)如何使用 https**

(之前 angular 开发的时候，前端项目有配 ssl 启动，但后来 vue 就是 `http://localhost`，然后 https 访问后台，并无警告)

- 使用 [mkcert](https://github.com/FiloSottile/mkcert) 为本地开发创建 TLS 证书,为本地网站开启 HTTPS(推荐)
- 找到基于由实际证书颁发机构（而不是本地机构）签署证书的技术(例如[Let's Encrypt](https://letsencrypt.org/zh-cn/))
- 自签名证书,openssl 等其他工具生成证书(与 Let's Encrypt 等不同，自签名证书可能很多现代浏览器不认)
- 使用反向代理，例如 [ngrok(https://ngrok.com/) 。

## HTTPS 进行安全连接

**HTTPS 为何重要**

- HTTPS 可帮助阻止入侵者**篡改**网站与用户浏览器间的**通信**（入侵可能发生在网络中的任何一环）。
  - 入侵者包括故意的恶意攻击者，以及合法但具有侵入性的公司，例如 ISP 或在网页中植入广告的酒店。
  - 入侵者利用未受保护的通信来诱使用户放弃敏感信息或安装恶意软件，或者将他们的广告插入资源中。
  - 入侵者会利用在网站和用户之间传输的所有未受保护的资源，包括图像、cookie、脚本、HTML……
- HTTPS 可防止入侵者**被动监听**网站与用户之间的**通信**。
  - 事实上每个未受保护的 HTTP 请求都可能泄露有关用户行为和身份的信息。
  - 一些入侵者会查看用户的总体浏览活动，从而推断他们的行为和意图，并对他们的身份进行去匿名化。
- HTTPS 是一些现代化 web 新功能和更新 API 的**权限工作流的关键组成**部分。
  - 一些新的 Web 平台功能十分强大，例如`getUserMedia()`、Service Worker。这些功能在执行之前都需要用户的明确许可。

**在服务器上启用 HTTPS**

- 创建一个 2048 位的 RSA 公钥/私钥对。
- 生成一个包含公钥的证书签署请求（CSR）。
- 与证书颁发机构（CA）分享 CSR，以获得最终证书或证书链。
- 将最终证书安装在一个非网络可访问的地方，如`/etc/ssl`（Linux 和 Unix）或 IIS 要求的地方（Windows）

nginx 配置 https 的示例（需要`ngx_http_ssl_module`模块(自带)）。

```conf
server {
    listen 443 ssl http2;     # 配置https服务器，需要在此启用ssl参数，启用http2
    ssl_certificate /root/install/nginx/server.crt;     # 指定服务器证书的位置
    ssl_certificate_key /root/install/nginx/server.key;     # 指定私钥文件的位置
    ssl_protocols TLSv1.2 TLSv1.3; # 用于将连接限制为仅包括 SSL/TLS 的强版本和密码
    ssl_ciphers HIGH:!aNULL:!MD5; # 指定启用的密码。密码以 OpenSSL 库可以理解的格式指定
    ## …… 其他配置
  }
```

**混合内容(mixed content)**

通过安全 HTTPS 连接加载初始 HTML，但通过不安全的 HTTP 连接加载其他资源（如图像、视频、样式表、脚本）时，就会出现**混合内容**。  
不仅仅是因为显示的*同一个页面上同时加载了 HTTP 和 HTTPS 内容*，还因为*初始请求是通过 HTTPS 加密的*。

使用不安全的 HTTP 协议请求子资源会降低整个页面的安全性，因为这些请求容易遭受 **[路径中攻击](https://www.ietf.org/rfc/rfc7835.html#section-2.1.1)**。攻击者会窃听网络连接并查看或修改两方之间的通信。利用这些资源，攻击者可以跟踪用户并替换网站上的内容。而对于主动混合内容的情况，他们可以完全控制页面，而不仅仅是导致资源不安全。

**被动混合内容**是指*不与页面其余部分交互的内容*，因此，中间人攻击将仅限于他们拦截或更改这种内容时可以执行的操作。被动混合内容包括图像、视频和音频内容。**主动混合内容** _作为一个整体与页面进行交互，因此允许攻击者对页面执行几乎任何操作_。主动混合内容包括脚本、样式表、iframe 和浏览器可以下载和执行的其他代码。

**修复混合内容**

网站支持 HTTPS 是保护网站和用户免受攻击的一项重要举措，但混合内容会使这种保护失效。

在 Google Chrome 中访问 HTTPS 网页时，浏览器会在 JavaScript 控制台中以错误和警告的形式提醒您存在混合内容。

- 被动混合内容将给出警告。如果浏览器能够在 https URL 找到被动混合内容，会自动将其升级，然后显示一条消息。
- 浏览器会阻止主动混合内容并显示一条错误。(都显示`Mixed Content: The page at ……`)

**修复混合内容的措施**，就是**把所有 http 的资源改成 https**。如果无法通过 `https://` 获得资源，则需要补足资源或者删除与替代。  
类似`<a>`等标准标签 URL 不会导致混合内容错误；然而，一些图像库脚本会覆盖 `<a>` 标签的功能，并将 href 属性指定的 HTTP 资源加载到网页上的灯箱显示中，从而导致发生混合内容问题。

**CSP 报告机制可用于跟踪网站上的混合内容，并提供执行策略，通过升级或阻止混合内容来保护用户。**

1. 通过 `Content-Security-Policy-Report-Only`响应体，使用内容安全策略来**收集网站上混合内容的报告**:

```sh
Content-Security-Policy-Report-Only: default-src https: 'unsafe-inline' 'unsafe-eval'; report-uri https://example.com/reportingEndpoint
# report-uri 响应头已被弃用，取而代之的是 report-to。支持 report-to 的浏览器目前只有 Chrome 和 Edge。您可以同时提供上述两个标头，如果浏览器支持 report-to，则会忽略 report-uri。
# 每当用户访问您网站上的网页时，他们的浏览器都会向 https://example.com/reportingEndpoint 发送一份 JSON 格式的报告，【列举违反内容安全策略的内容。此时，只要通过 HTTP 加载子资源，就会发送报告。】
```

**注意事项**: 1 用户必须在能够识别 CSP 标头的浏览器中访问您的网页。2 只能获得用户访问过的网页的报告(流量不太多时则报告获取时间久)。

2. 使用 CSP 指令**让浏览器把一个网站所有的不安全 URL（通过 HTTP 访问）当做已经被安全的 URL 链接（通过 HTTPS 访问）替代。**

配置响应头，或者在`<head>`中配置`<meta>`元素，会级联到 `<iframe>` 文档中，确保整个网页都受到保护:

```sh
Content-Security-Policy: upgrade-insecure-requests
<meta  http-equiv="Content-Security-Policy"  content="upgrade-insecure-requests"/>
```

3. 阻止所有混合内容。（所有混合内容资源请求都会被阻止，包括主动和被动混合内容。）

```sh
Content-Security-Policy: block-all-mixed-content # 优先级比上一个低
<meta http-equiv="Content-Security-Policy" content="block-all-mixed-content">
```

**开发环境使用 https 的情况**

- 在使用`Set-Cookie`响应头时设置了选项为`Secure`、`SameSite:none`或者`__Host`的 cookie。
  - `Secure`选项只能用于 https，`SameSite:none`和`__Host`需要 cookie 是`Secure`
- 需要在本地调试一个**只出现在 HTTPS 网站**上而不会出现在 HTTP 网站上的问题(例如混合内容)。
- 需要在本地测试或重现**特定于 HTTP/2 或更高版本的行为**(比如测试 http2 的加载性能)。
- 需要在本地测试需要 **HTTPS 的第三方库或 API**（例如 OAuth）。
- 使用的不是 localhost，而是用于本地开发的**自定义主机名**(修改了本机 host 文件)

**开发环境(本地)如何使用 https**

(之前 angular 开发的时候，前端项目有配 ssl 启动，但后来 vue 就是 `http://localhost`，然后 https 访问后台，并无警告)

- 使用 [mkcert](https://github.com/FiloSottile/mkcert) 为本地开发创建 TLS 证书,为本地网站开启 HTTPS(推荐)
- 找到基于由实际证书颁发机构（而不是本地机构）签署证书的技术(例如[Let's Encrypt](https://letsencrypt.org/zh-cn/))
- 自签名证书,openssl 等其他工具生成证书(与 Let's Encrypt 等不同，自签名证书可能很多现代浏览器不认)
- 使用反向代理，例如 [ngrok(https://ngrok.com/) 。

## 防止信息泄露

**浏览器沙箱模式(browser sandbox)**

- 现代网络浏览器建立在“沙箱”的概念之上。**沙箱是一种用于在受限环境中运行应用程序的安全机制。**应用程序代码可以在受限环境中自由执行。
- _操作系统层面的沙箱_:操作系统对进程的可访问的内存地址所做的限制，限制进程可访问的内存在其被分配的内存地址区间内，而不允许操作其他的内存地址，从而提供安全层面的防护。
- _浏览器层面的沙箱_:限制脚本操作本页面之外的其他页面的 DOM，限制访问非同源文档，限制向非同源服务器发送 ajax 等，目的依然是安全。
- **浏览器沙箱是通过使运行任意代码更安全而使 Web 浏览顺畅的关键功能。**
- 浏览器也可能存在漏洞，攻击者总是试图绕过沙箱（例如使用[Spectre Attack](https://developer.chrome.com/blog/meltdown-spectre/)）。
- 沙盒有时会妨碍创建出色的 Web 体验。例如，浏览器可能会阻止对托管在不同域上的图像的获取请求。

**同源策略(same-origin policy)**

- 同源策略是一个浏览器的安全功能，它**限制了一个源的文件(documents)和脚本(scripts)如何与另一个源的资源互动(interact)**。
- 同源策略通过阻止对从不同源加载的资源的读取访问来防止脚本被攻击者破坏。
  - 浏览器允许一些标签(例如 frame)嵌入来自不同来源的资源，但可能把网站暴露于漏洞，遭受例如使用 iframe 的点击劫持。

**一般来说，允许嵌入跨域资源，而阻止读取跨域资源。**  
Generally, **embedding** a cross-origin resource is **permitted**, while **reading** a cross-origin resource is **blocked**.

|            |                                                                                                                                  |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------- |
| iframes    | 跨源嵌入通常是**允许**的（`X-Frame-Options` 值为`SAMEORIGIN`时），但跨源阅读（如使用 js 访问 iframe 中的文档）则**不允许**。     |
| CSS        | 跨源 CSS **可以**使用`<link>`元素或 CSS 文件中的`@import`来嵌入。可能需要正确的`Content-Type`标头。                              |
| forms      | 跨源 URL **可以**作为表单元素的`action`属性值。网络应用程序可以将表单数据写到一个跨源目的地。                                    |
| images     | 嵌入跨源图像是**允许**的(例如使用`<img>`标签的`src`属性)。读取跨源图像数据（如使用 js 检索跨源图像的二进制数据）是被**禁止**的。 |
| multimedia | 跨源视频和音频**可以**使用`<video>`和`<audio>`元素进行嵌入。                                                                     |
| script     | 跨源脚本**可以**被嵌入；但是，对某些 API 的访问（如跨源获取请求）**可能被阻止**。                                                |

**点击劫持(Clickjacking)**

将网站嵌入到 iframe 链接到不同目的地的透明按钮上。用户在向攻击者发送数据时被欺骗以为他们正在访问您的应用程序。

阻止其他网站将您的网站嵌入 iframe(设置 Content-Security-Policy 和 X-Frame-Options 响应头):

- HTTP CSP 标头指定可以包含`<iframe>`等标签的源:
  - `Content-Security-Policy:frame-ancestors <source> <source>;`
- 使用`X-Frame-Options`标头给浏览器指示是否允许一个页面展示`<frame>`、`<iframe>`、`<embed>`或者`<object>`中的标记。

**跨域资源共享 (CORS)**

CORS **一般运作步骤**

- 第一步：客户端（浏览器）请求: 当浏览器发出跨域请求时，该浏览器会添加一个包含当前源（协议、主机和端口）的 `Origin` 标头。
- 第二步：服务器响应: 在服务器端需要在响应中加入一个`Access-Control-Allow-Origin` 标头来指定请求源（或加入\*来允许任何源。）
- 第三步：浏览器接收响应: 当浏览器看到带有相应 `Access-Control-Allow-Origin` 标头的响应时，即允许与客户端网站共享响应数据。

CORS 通常用于“匿名请求”，即不识别请求方的请求。如果**想在使用 CORS 时发送 cookie**(这样会识别发送者),需要添加额外的标头。

- 将`credentials: 'include'`添加到请求的配置选项中。该操作将包括请求中的 cookie。
- 响应头`Access-Control-Allow-Origin`必须设置一个特定的源，且`Access-Control-Allow-Credentials`必须设置为`true`。

CORS 规范将**复杂请求**定义为

- 使用除 GET、POST 或 HEAD 以外方法的请求
- 包含除 `Accept`、`Accept-Language` 或 `Content-Language` 以外标头的请求
- 具有除 application/x-www-form-urlencoded、multipart/form-data 或 text/plain 以外的`Content-Type`标头的请求

复杂请求**预先检查**

- 浏览器会根据需要创建预检请求。真实请求发出之前，先发出一个 OPTIONS 请求。
- 在服务器端，应用程序在响应预检请求时需要提供程序从该源接受的方法的相关信息。
- 服务器响应还可以包含一个`Access-Control-Max-Age`标头，用于指定缓存预检结果的持续时间（以秒为单位）

更多内容，参看[跨域资源共享 (CORS)](#jump-cors)

**使用 COOP 和 COEP“跨源隔离”网站**

使用 COOP 和 COEP 设置跨源隔离环境并启用强大的功能，如“SharedArrayBuffer”、  
“performance.measureUserAgentSpecificMemory()”以及更高精度的高解析性能计时器。

**某些 Web API 会导致 Spectre 等旁道攻击的风险增加**。为了减轻这种风险，浏览器提供了一个基于选择的隔离环境(opt-in-based isolated environment)，称为 **“跨源隔离”**。

在跨源隔离状态下，网页能够使用特权功能，包括：

- [SharedArrayBuffer](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer): WebAssembly 线程需要
- [performance.measureUserAgentSpecificMemory()](https://web.dev/monitor-total-page-memory-usage/): Chrome 89 中提供,监控网页的总内存使用情况
- [performance.now(),performance.timeOrigin](https://bugs.chromium.org/p/chromium/issues/detail?id=1180178): 通过跨源隔离，解析时间可以达到 5 微秒或更短。

**跨源隔离状态还可以防止修改`document.domain`**.(如果能够修改`document.domain`则允许同站文档之间相互通信，这是同源策略中的一个漏洞)

**启用跨域隔离**(cross-origin isolated)

```sh
Cross-Origin-Embedder-Policy: require-corp # 文档只能从相同的源加载资源，或显式标记为可从另一个源加载的资源。
Cross-Origin-Opener-Policy: same-origin # 将浏览环境完全隔离于同源文件。跨源文件不会在同一浏览环境中加载。
```

通过检查 [self.crossOriginIsolated](https://developer.mozilla.org/zh-CN/docs/Web/API/crossOriginIsolated) 来确定网页是否处于跨源隔离状态。

**需要“跨源隔离”的原因**

- COEP：Cross-Origin Embedder Policy - 跨源嵌入器策略
- COOP：Cross-Origin Opener Policy - 跨源打开程序策略
- CORP：Cross-Origin Resource Policy - 跨源资源策略
- CORS：Cross Origin Resource Sharing - 跨源资源共享
- CORB：Cross Origin Read Blocking - 跨源读取阻塞

长期以来，CORS 和不透明资源的结合足以让浏览器变得安全。总体而言，不允许直接读取跨域资源原始字节的原则是成功的。

但由于 Spectre 漏洞，这使得加载到与您的代码相同的浏览上下文组的任何数据都可能具有可读性。通过测量某些操作所花费的时间，攻击者可以猜测 CPU 缓存的内容，进而猜测进程内存的内容。

**Spectre 是一个漏洞，可诱使程序访问程序内存空间中的任意位置。攻击者可能会读取访问内存的内容，从而可能获取敏感数据。**

理想情况下，所有跨域请求都应该由拥有资源的服务器明确审查(explicitly vetted)。  
**如果资源拥有服务器不提供审查，那么数据将永远不会进入恶意行为者的浏览上下文组，因此将远离网页可能执行的任何 Spectre 攻击。我们称之为跨域隔离状态。**这正是 COOP+COEP 的意义所在。

_在跨域隔离状态下，请求站点被认为不那么危险_，这解锁了强大的功能，  
例如 `performance.measureUserAgentSpecificMemory()`、SharedArrayBuffer、和具有更高精度的[高分辨率计时器](https://www.w3.org/TR/hr-time/)，否则这些功能可用于类似 Spectre 的攻击。它还可以防止修改 `document.domain` 。

**使用 Fetch Metadata 保护资源免受 Web 攻击**

许多 Web 应用程序容易受到跨源攻击，例如跨站点请求伪造(CSRF)、跨站点脚本包含(XSSI)、定时攻击、跨源信息泄漏或推测执行侧信道(Spectre)攻击。

典型的跨源攻击是**跨站点请求伪造 (CSRF)**，

- 攻击者将用户引诱到他们控制的站点，然后向用户登录的服务器提交表单。
- 由于*服务器无法判断请求是否来自另一个域（跨站点）*，并且浏览器会自动将 cookie 附加到跨站点请求，因此服务器将代表用户执行攻击者请求的操作。
- 将[CSRF 令牌](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html#token-based-mitigation)作为您的主要保护措施。要想获得额外保护，请使用 SameSite，同时使用诸如 Origin（可用于 POST 和 CORS 请求）和 Sec-Fetch-Site（如果可用）这样的标头，而不是 Referer。

**跨站点脚本包含 (XSSI)** 或*跨源信息泄漏*，本质上与 CSRF 类似，并依赖于从受攻击者控制的文档中的受害应用程序加载资源并泄漏有关受害应用程序的信息。_由于应用程序无法轻易区分可信请求和不可信请求，因此它们无法丢弃恶意的跨站点流量。_

`Fetch Metadata 请求标头`允许您部署强大的纵深防御机制——"资源隔离策略"——以保护您的应用程序免受这些常见的跨源攻击。

并非所有浏览器都支持该标头，因此需要通过检查请求的`sec-fetch-site`的存在来允许未设置`Sec-Fetch-*`标头的请求。基于 Chromium 都支持。

`Fetch Metadata 请求标头`是一个 HTTP 请求标头，**提供有关发起请求的上下文的附加信息。这允许服务器根据请求的来源以及资源的使用方式来决定是否应允许请求。**

该标头包含以下四个:

- Sec-Fetch-Site:表明了一个请求发起者的来源与目标资源来源之间的关系。服务器可以选择接受或拒绝。有 4 个可选值:
  - `cross-site`: 请求发起者和托管资源的服务器具有**不同的站点** (由另一个网站发送的请求)
  - `same-origin`: 请求发起者和托管资源的服务器具有**相同的来源**(相同的方案、主机和端口)(自己的应用程序发出的请求)
  - `same-site`: 请求发起者和托管资源的服务器具有**相同的方案、域和/或子域，但不一定具有相同的端口。**(站点的子域发出的请求)
  - `none`: 此请求是**用户发起的操作**。用户与用户代理的交互（例如点击书签）明确引起的
- Sec-Fetch-Mode: 表明了一个请求的模式。大致对应于请求的类型，并允许您区分资源负载和导航请求。有 5 个可选值:
  - `cors`:该请求是 CORS 协议请求。
  - `navigate`: 该请求由 HTML 文档之间的导航启动(顶层导航请求)。
  - `no-cors`: 该请求是一个无证书请求(例如加载图像等资源请求)。
  - `same-origin`: 请求来自与被请求资源相同的来源。
  - `websocket`: 正在发出建立 WebSocket 连接的请求。
- Sec-Fetch-User: 表明了一个导航请求是否由用户激活触发。
  - 该值将始终为`?1`。当请求**不是由用户**激活触发时，规范要求浏览器完全**省略标头**。
  - 只在 [navigation-request](https://fetch.spec.whatwg.org/#navigation-request)(destination is "document", "embed", "frame", "iframe", or "object"的请求)时触发。
- Sec-Fetch-Dest: 即数据的来源以及如何使用这些获取到的数据。可选值对应[Request.destination](https://developer.mozilla.org/en-US/docs/Web/API/Request/destination)返回的值。
  - audio, audioworklet, document, embed, font, frame, iframe, image, manifest, object, paintworklet, report, script, sharedworker, style, track, video, worker or xslt
  - 其中说明几个。`empty`: 目标是空字符串。这用于没有自己值的目标。例如：fetch()、navigator.sendBeacon()、EventSource、XMLHttpRequest、WebSocket 等等。
  - `font`:目标是字体。这可能源自 CSS `@font-face`。
  - `serviceworker`:目标是 service worker。这可能源于对 `navigator.serviceWorker.register()` 的调用。
  - `video`:目标是视频数据。这可能源自于 `<video>` 标签。
  - 标头包含任何其他的值(非[Request.destination](https://developer.mozilla.org/en-US/docs/Web/API/Request/destination)返回的值)，服务器应忽略它。

这些请求标头提供的额外信息非常简单，但额外的上下文允许您在服务器端构建强大的安全逻辑，也称为**资源隔离策略**

**实施资源隔离策略**

- 资源隔离策略可防止您的资源被外部网站请求。阻止此类流量可缓解常见的跨站点 Web 漏洞，例如 CSRF、XSSI、定时攻击和跨源信息泄漏。
- 可以为您的应用程序的所有端点启用此策略，并将允许来自您自己的应用程序的所有资源请求以及直接导航（通过 HTTP GET 请求）。
- 应该在跨站点上下文中加载的端点（例如使用 CORS 加载的端点）可以选择退出此逻辑
- (实际就是根据 Fetch Metadata 请求标头的各个选项以及值，在后台对应控制该请求是否被允许)

**部署资源隔离策略**

- 安装“实现了资源隔离策略”的模块，用于记录和监控您网站的行为，并确保这些限制不会影响任何合法流量。
- 通过免除合法的跨源端点来修复潜在的违规行为。
- 通过丢弃不合规的请求来加强策略。

**识别和修复违反策略的行为**

- 首先在服务器端代码中以报告模式启用策略，从而以无副作用的方式对其进行测试。
- 或者可以在中间件或反向代理中实现此逻辑，反向代理会记录策略在应用于生产流量时可能产生的任何违规行为。

**加强资源隔离策略**

- 在确认*策略不会影响合法的生产流量*之后，就可以加强限制了，以保证其他站点将无法请求资源，并保护用户免受跨站点攻击。
- 确保在运行身份验证检查或对请求进行任何其他处理之前拒绝无效请求，以防止泄露敏感的时间信息。

## 保护网站免受 XSS 攻击

**使用 Trusted Types 防止基于 DOM 的跨站点脚本漏洞**

基于 DOM 的跨站点脚本 (DOM XSS) 是最常见的 Web 安全漏洞之一，并且您的应用程序很容易将其引入。  
Trusted Types 默认对危险的 Web API 函数加以保护，从而提供了编写、安全审核和维护无 DOM XSS 漏洞的应用程序的工具。  
Chrome 83 支持 Trusted Types，其他浏览器可以使用 polyfill。参阅[浏览器兼容性](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/trusted-types)。

为了防止服务器端 XSS，**不要通过连接字符串来生成 HTML**，而是使用安全的上下文自动转义模板库。  
浏览器还可以通过 Trusted Types 帮助防止客户端（也称为基于 DOM）XSS。

**Trusted Types 的工作原理**是锁定以下有风险的接收器函数:

- 脚本操作：`<script src>` 和设置 `<script>` 元素的文本内容。
- 从字符串生成 HTML ：innerHTML、outerHTML、insertAdjacentHTML、`<iframe> srcdoc`、document.write、document.writeln 和 DOMParser.parseFromString
- 执行插件内容：`<embed src>`、`<object data>` 和 `<object codebase>`
- 运行时 JavaScript 代码编译：eval、setTimeout、setInterval、new Function()

_Trusted Types 要求在将数据传递给上述接收器函数之前对其进行处理_。仅使用字符串将失败，因为浏览器不知道数据是否可信。

**使用 Trusted Types**

- 准备内容安全策略违规报告:可以部署报告收集器,还可以在浏览器中调试违规.
- 添加仅报告 CSP 标头:
  - `Content-Security-Policy-Report-Only: require-trusted-types-for 'script'; ...`
- 识别 Trusted Types 违规: 分析报告中违规细节。
- 修复违规: 重写违规代码，使用库(例如[DOMPurify](https://github.com/cure53/DOMPurify))，创建 Trusted Type 策略，或者"创建默认策略"作为最后手段。
- 使用默认策略:有时无法更改出错的代码(从 CDN 加载第三方库)，这种情况使用默认策略
  - `trustedTypes.createPolicy('default', {...});`
  - 只要在仅接受 Trusted Type 的接收器中使用字符串，就会使用名为 `default` 的策略。
- 切换到强制执行内容安全策略: 当应用程序不再产生违规时，可以开始强制执行 Trusted Types
  - (设置 CSP 头:`Content-Security-Policy: require-trusted-types-for 'script';`)

**使用严格的内容安全策略 (CSP) 缓解跨站点脚本 (XSS)**

**严格 CSP** _是使用基于随机数或散列的 CSP_ 来缓解 XSS，而不是常用的基于主机允许列表的 CSP，后者通常会使页面暴露于 XSS，因为它们可以在大多数配置中被绕过。

当应用程序使用严格的 CSP 时，发现 HTML 注入漏洞的攻击者通常无法使用它们来强制浏览器在易受攻击的文档的上下文中执行恶意脚本。  
这是因为**严格的 CSP 只允许在服务器上生成散列脚本或具有正确 nonce 值的脚本**，因此攻击者无法在不知道给定响应的正确 nonce 的情况下执行脚本。

白名单 CSP 不足: 在大多数配置中可以绕过它;需要大量的定制。
严格的 CSP 优点: 基于加密随机数或散列;始终具有相同的结构。

**严格的 CSP 结构**

```sh
# 基于 Nonce 的严格 CSP 和 基于哈希的严格 CSP； 严格 CSP 的最精简版本
Content-Security-Policy:script-src 'nonce-{RANDOM}' 'strict-dynamic';object-src 'none';base-uri 'none';
Content-Security-Policy:script-src 'sha256-{HASHED_INLINE_SCRIPT}' 'strict-dynamic'; object-src 'none'; base-uri 'none';
```

_以下属性使 CSP 与上述“严格”类似_，因此是安全的:

- 使用 "nonce-{RANDOM}"或 "sha256-{HASHED_INLINE_SCRIPT}"来表明哪些`<script>`标签受到网站开发者的信任，应该被允许在用户的浏览器中执行。
- 设置 "strict-dynamic"，通过自动允许执行由已被信任的脚本创建的脚本，减少部署基于 nonce 或 hash 的 CSP 的努力。这也解除了对大多数第三方 JavaScript 库和小工具的使用限制。
- 不基于 URL 允许列表，因此不会受到[常见的 CSP 绕过](https://speakerdeck.com/lweichselbaum/csp-is-dead-long-live-strict-csp-deepsec-2016?slide=15)的影响。
- 阻止不受信任的内联脚本，如内联事件处理程序或`javascript:` URIs。
- 限制`object-src`以禁用危险的插件，如 Flash。
- 限制`base-uri`，阻止`<base>`标签的注入。这可以防止攻击者改变从相对 URL 加载的脚本的位置。

**采用严格的 CSP**

- 决定你的应用程序是否应该设置一个基于`nonce`的或哈希的 CSP。
- 参看上面“严格的 CSP 结构”构建 CSP，并将其设置为整个应用程序的响应头。
- 重构 HTML 模板和客户端代码，删除与 CSP 不兼容的模式。
- 增加回退功能，以支持 Safari 和旧的浏览器。(设置 CSP 头的 'unsafe-inline'值，如果设定了 nonce or hash 则会被忽略)
- 部署设定好的 CSP( 确定 CSP 不会导致最终用户损坏，请使用`Content-Security-Policy`响应标头部署您的 CSP)

**限制**

根据使用的 CSP 的类型（随机数、散列、带或不带'strict-dynamic'），在**某些情况下 CSP 不保护**：

- 如果你对一个脚本进行了 nonce，但有一个直接注入到正文或该`<script>`元素的 src 参数中。
- 如果在动态创建的脚本（document.createElement('script')）的位置有注入，包括注入任何基于其参数值创建脚本 DOM 节点的库函数。
  - 这包括一些常见的 API，如 jQuery 的.html()，以及 jQuery < 3.0 的.get()和.post()。
- 如果在旧的 AngularJS 应用程序中存在模板注入的情况
- 如果策略中包含 "unsafe-eval"，则在使用 eval()、setTimeout()和其他一些很少使用的 API 时出现进行注入的情况。

## 保护用户免受跟踪

**隐私沙盒(privacy Sandbox)**

隐私沙盒是一系列在没有第三方 cookie 或其他跟踪机制的情况下满足第三方用例的建议。  
隐私沙盒引入了一组隐私保护 API，以支持在缺乏第三方 cookie 等跟踪机制的情况下为开放网络提供资金的商业模式。  
隐私沙盒 API 要求 Web 浏览器承担新角色。API 不是使用有限的工具和保护措施，而是使用户的浏览器能够代表用户（在本地、在他们的设备上）执行操作，以在用户浏览 Web 时保护用户的识别信息。

**[Set-Cookie](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Headers/Set-Cookie)响应头及其 SameSite 指令说明**

`Set-Cookie` HTTP 响应头用于从服务器向用户代理发送 cookie，以便用户代理稍后可以将其送回服务器。要发送多个 cookie，应在同一个响应中发送多个 Set-Cookie 头。

警告: 根据 Fetch 规范，Set-Cookie 是一个[禁止的响应标头](https://fetch.spec.whatwg.org/#forbidden-response-header-name)，对应的响应在被暴露给前端代码前，必须滤除这一响应标头，即浏览器会阻止前端 JavaScript 代码访问 Set-Cookie 标头。

注意设置`Set-Cookie`响应标头及相关属性配置的[浏览器兼容性](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#browser_compatibility)

语法:`Set-Cookie: <cookie-name>=<cookie-value>; Domain=<domain-value>; Secure; HttpOnly`,可用指令如下:

- 必选 `<cookie-name>=<cookie-value>`,一个 cookie 开始于一个名称/值对。其中特殊前缀的 cookie-name 有特定含义:
  - **`__Secure-`**: 该 cookie 必须与`secure`属性一同设置，同时必须应用于安全页面（即使用 HTTPS 访问的页面）。
  - **`__Host-`**: 该 cookie 必须与`secure`属性一同设置，必须应用于安全页面，禁止设置`domain`,同时`path`的值必须为`/`。
- `Expires=<date>`: cookie 的最长有效时间，形式为符合 HTTP-date 规范的时间戳(截止时间与客户端相关)。
- `Max-Age=<number>`: 在 cookie 失效之前需要经过的秒数。秒数为 0 或 -1 将会使 cookie 直接过期。优先级比`Expires`高。
- `Domain=<domain-value>`: 指定 cookie 可以送达的主机名。默认值为当前文档访问地址中的主机部分（但是不包含子域名）
- `Path=<path-value>`: 指定一个 URL 路径，这个路径**必须**出现在要请求的资源的路径中才可以发送 Cookie 标头。
  - `/`为文件目录分隔符:`path=/docs`，则`/docs`、`/docs/`、`/docs/Web/`和`/docs/Web/HTTP` 都满足匹配条件。
- `Secure`: 一个带有安全属性的 cookie 只有在请求使用 `https:` 协议（localhost 不受此限制）的时候才会被发送到服务器
- `HttpOnly`:用于阻止 JavaScript 通过 Document.cookie 属性访问 cookie。在 js 初始化的请求中仍然会被发送。
- `SameSite=<samesite-value>`: 允许服务器设定一则 cookie 不随着跨站请求一起发送，可以在一定程度上防范（CSRF）,有 3 个值:
  - `Lax`: Cookies 允许与顶级导航一起发送，并将与第三方网站发起的 GET 请求一起发送。这是*浏览器中的默认值*。
  - `Strict`: Cookies 只会在第一方上下文中发送，不会与第三方网站发起的请求一起发送。
  - `None`: Cookie 将在所有上下文中发送，即允许跨站发送。(使用 None 时，需在最新的浏览器版本中使用 `Secure` 属性)

**SameSite cookie 的说明**

与当前网站的域名(浏览器地址栏中显示的内容)相匹配的 cookie 被称为**第一方 cookie**。来自当前网站以外域名的 cookie 被称为**第三方 cookie**。

_这不是一个绝对的标签，而是相对于用户上下文来决定的_。同一个 cookie 可以是第一方的，也可以是第三方的，具体取决于用户当时所在的网站。

例如:假设您有一个博客，您想在其中向用户显示"最新消息"的宣传。用户可以选择不看这则宣传，然后在一段时间内，他们就不会再次看到这则宣传。可以这样设置 cookie:`Set-Cookie: promo_shown=1; Max-Age=2600000; Secure`。当您的读者查看的页面满足这些要求，即他们处于安全连接上且 cookie 还不到一个月，那么他们的浏览器将在其请求中发送此标头：
`Cookie: promo_shown=1`。
假设您的一篇博文中有一张非常独特的猫的照片，而这张照片被托管在`/blog/img/amazing-cat.png`。因为照片十分令人惊叹，其他人直接在他们的网站上使用了该照片。
如果访问者访问过您的博客并拥有`promo_shown` cookie，那么当他们在其他人的网站上浏览`amazing-cat.png`时，就会在图像请求中发送该 cookie。
这对任何一方都不是特别有用，因为`promo_shown`在其他人的网站上不用于任何内容，只是增加了请求的开销。

Chrome(84 稳定版以后)、Firefox 、Edge 和其他浏览器将根据 IETF 提案 Incrementally Better Cookies 更改其默认行为，因此：

- 不带 SameSite 属性的 cookie 将被视为 `SameSite=Lax`，这意味着默认行为将 cookie 限制到**仅**第一方上下文。
- 跨网站使用的 Cookie 必须指定 `SameSite=None; Secure` 才能包含在第三方上下文中。

> Strict 和 Lax 都不是针对您的网站安全的完整解决方案。Cookie 是作为用户请求的一部分发送的，而您应该像对待任何其他用户输入一样对待 cookie。这就意味着要对这些输入进行清理和验证。切勿使用 cookie 来存储您认为是服务端机密的数据。

**跨站点或第三方 cookie 的用例**

1. `<iframe>` 中显示的其他网站的内容在第三方上下文中:

- 共享自其他网站的嵌入内容，例如视频、地图、代码示例和社交媒体帖子。
- 来自外部服务的小工具，例如付款、日历、预订和预约功能。
- 会创建不太明显的 `<iframes>` 的社交媒体按钮或反欺诈服务等小工具。

这里，Cookie 可用于保持会话状态、存储常规偏好、启用统计或为拥有现有帐户的用户提供个性化内容等。

2. 跨网站的“不安全”请求

- 这里指的是可能要更改状态的请求。在 Web 上主要是 POST 请求。
  - 标记为 `SameSite=Lax` 的 cookie 将在安全的顶级导航中发送，例如单击一个链接转到其他网站。
  - 但是，通过 POST 向其他网站提交 `<form>` 等行为不会包括 cookie。
- 此模式用于可能将用户重定向到远程服务执行某些操作再返回的网站，例如重定向到第三方身份提供商。
  - 在用户离开网站之前，会设置一个包含一次性令牌的 cookie，期望可以在返回请求中检查此令牌，以缓解跨站点请求伪造 (CSRF) 攻击。
  - 如果该返回请求通过 POST 传入，则有必要将 cookie 标记为` SameSite=None; Secure`。

3. 远程资源

- 页面上的任何远程资源都可能依赖于随请求发送的 cookie、来自 `<img>` 标签、`<script>` 标签等。
  - 常见用例包括追踪像素和个性化内容。这也适用于由 fetch 或 XMLHttpRequest 从 JavaScript 发起的请求
  - 如果调用 fetch() 时带有 `credentials: 'include'` 选项，那么这是表明这些请求很可能需要 cookie 的好迹象。
  - 对于 XMLHttpRequest，您应该查找 withCredentials 属性设置为 true 的实例。这是表明这些请求很可能需要 cookie 的好迹象。这些 cookie 需要适当标记以包含在跨网站请求中。

4. WebView 中的内容

- 平台特定的应用程序中的 WebView 是由浏览器驱动的，您需要测试相同的限制或问题是否适用。
- 与通过标头或 JavaScript 设置的 cookie 一样，如果要跨网站使用 cookie，请考虑包含 `SameSite=None; Secure`。

**目前如何实施 SameSite**

- 对于只有第一方上下文中需要的 cookie，理想情况下，应该根据需要将它们标记为 `SameSite=Lax` 或 `SameSite=Strict`
- 对于第三方上下文中需要的 cookie，您需要确保将它们标记为 `SameSite=None; Secure`。
  - 请注意，您需要同时标记这两个属性。如果只指定 None 而没有指定 Secure，cookie 将被拒绝。
- [在 Node.js 中处理不兼容的客户端的示例](https://web.dev/i18n/en/samesite-cookie-recipes/#handling-incompatible-clients)

**第一方 cookie 的配置示例**

```sh
Set-Cookie:
__Host-cookie-name=cookie-value; # __Host是一个可选前缀，它使某些属性成为必需属性并禁止其他属性
Secure;   # Secure必填，Domain必省略(省略它会将 cookie 限制为当前文档主机，不包括子域)，Path一定要是/
Path=/;
HttpOnly; # 用于阻止 JavaScript 通过 Document.cookie 属性访问 cookie。
Max-Age=7776000; # cookie的有效时长，单位 秒
SameSite=Lax; # cookie 不会在跨站请求中被发送，但在用户从外部站点导航到源站时(如点击链接)，cookie 也将被发送
```

**具有子域的第一方 cookie 的配置示例**

```sh
Set-Cookie:
__Secure-cookie-name=cookie-value; # 想在所有的子域上有一个用户会话(session)，__Host前缀限制太死
Secure; # __Secure只要求cookie被设置为Secure，但要指定 Domain 域名
Domain=news.site;
Path=/;
HttpOnly;
Max-Age=7776000;
SameSite=Lax;
```

**限制第三方网站发起的请求访问第一方 cookie**

```sh
Set-Cookie:
__Host-cookie-name=cookie-value;
Secure;
Path=/;
HttpOnly;
Max-Age=7776000;
SameSite=Strict; # 浏览器仅对同一站点的请求发送 cookie
```

在跨方案(cross-scheme)的场景中(`https->http`，或`http->https`)，不同 SameSite 配置的 cookie 可达性不一。

- 在网站的跨方案版本之间导航: 例如，从 http ://site.example 链接到 https ://site.example
- 加载子资源。例如使用 XHR 或 Fetch 发出的图像、iframe 和网络请求。
- 发布表单如提交登录或签出表单时，与加载子资源一致。

| 网站的跨方案版本之间导航 | http→https | https→http | 加载子资源 或 提交表单 | http→https | https→http |
| ------------------------ | ---------- | ---------- | ---------------------- | ---------- | ---------- |
| SameSite=Strict          | 被封锁     | 被封锁     | SameSite=Strict        | 被封锁     | 被封锁     |
| SameSite=Lax             | 允许       | 允许       | SameSite=Lax           | 被封锁     | 被封锁     |
| SameSite=None;Secure     | 允许       | 被封锁     | SameSite=None;Secure   | 允许       | 被封锁     |

**Referer 和 Referrer-Policy 最佳实践**

注意`referer`标头是因为[原始规范中就写错](https://en.wikipedia.org/wiki/HTTP_referer)了，为了保持向下兼容就一直将错就错，其他例如`Referrer-Policy`则没有拼错。

_意外的跨域信息泄露是网络用户隐私的绊脚石_。一个保护性引荐来源政策(referrer policy)可以提供帮助。

可以考虑设置 `strict-origin-when-cross-origin` 的引荐来源政策。该政策保留了引荐来源的大部分用途，同时降低了跨域泄露数据的风险。

不要使用引荐来源来防范跨站请求伪造 (CSRF)，而是用 CSRF 令牌和其他标头作为额外的一层安全保障。

**Referer**

- Referer 请求头包含了当前请求页面的来源页面的地址，即表示当前页面是通过此来源页面里的链接进入的。
  - 服务端一般使用 Referer 请求头识别访问来源，可能会以此进行统计分析、日志记录以及缓存优化等。
- 以下两种情况下，Referer 不会被发送
  - 来源页面采用的协议为表示本地文件的 "file" 或者 "data" URI；
  - 当前请求页面采用的是非安全协议，而来源页面采用的是安全协议（HTTPS）。
- 语法`Referer: <url>`: `url`为当前页面被链接而至的前一页面的绝对路径或者相对路径。

**Referrer-Policy**

- Referer Policy HTTP 标头控制请求中应包含多少 Referer 信息（与 Referer 标头一起发送）。除了 HTTP 头之外，还可以在 HTML 中设置此策略。
- 通用头用法`Referrer-Policy: <directive>`，可选值有 8 个:
  - `no-referrer`: 整个 Referer 首部会被移除。访问来源信息不随着请求一起发送。
  - `no-referrer-when-downgrade`（默认值）在没有指定任何策略的情况下用户代理的默认行为。
    - 在同等安全级别的情况下，引用页面的地址会被发送 (HTTPS->HTTPS)，但是在降级的情况下不会被发送 (HTTPS->HTTP)。
  - `origin`: 在任何情况下，仅发送文件的源作为引用地址。
  - `origin-when-cross-origin`:对于同源的请求，会发送完整的 URL 作为引用地址，但是对于非同源请求仅发送文件的源
  - `same-origin`: 对于同源的请求会发送引用地址，但是对于非同源请求则不发送引用地址信息。
  - `strict-origin`: 在同等安全级别的情况下，发送文件的源作为引用地址 (HTTPS->HTTPS)，但是在降级的情况下不会发送 (HTTPS->HTTP)。
  - `strict-origin-when-cross-origin`: 对于同源的请求，会发送完整的 URL 作为引用地址；在同等安全级别的情况下，发送文件的源作为引用地址 (HTTPS->HTTPS)；在降级的情况下不发送此首部 (HTTPS->HTTP)。
  - `unsafe-url`: 无论是同源请求还是非同源请求，都发送完整的 URL（移除参数信息之后）作为引用地址。
  - 使用逗号分隔的列表，并将希望使用的策略放在最后：
    ```sh
    # no-referrer 仅在 strict-origin-when-cross-origin 不被浏览器支持的情况下被使用。
    Referrer-Policy: no-referrer, strict-origin-when-cross-origin
    ```
- 在 HTML 内设置 referrer 策略
  - 用一个 name 为 referrer 的 `<meta>` 元素为整个文档设置 referrer 策略。
    ```html
    <meta name="referrer" content="origin" />
    ```
  - 用`<a>`、`<area>`、`<img>`、`<iframe>`、`<script>`或者`<link>`元素上的`referrerpolicy`属性为其设置独立的请求策略。
    ```html
    <a href="http://example.com" referrerpolicy="origin"></a>
    ```
  - 可以在 `<a>`、`<area>` 或者` <link>` 元素上将 rel 属性设置为 `noreferrer`
    ```html
    <a href="http://example.com" rel="noreferrer"></a>
    ```
- 集成到 CSS:CSS 可以从样式表获取引用的资源，这些资源也可以遵从 referrer 策略
  - 外部 CSS 样式表使用默认策略 no-referrer-when-downgrade，除非 CSS 样式表的响应消息通过 Referrer-Policy 头覆盖该策略。
  - 对于 `<style>` 元素或 `style`属性，则遵从文档的 referrer 策略。

**为什么用 strict-origin-when-cross-origin（或更严格的政策）**

- **安全**:如果网站使用 HTTPS，则要杜绝网站的 URL 在非 HTTPS 请求中泄露。
  - no-referrer-when-downgrade、strict-origin-when-cross-origin、no-referrer 和 strict-origin 政策解决了中间人攻击问题。
- **隐私增强**:对于跨域请求，
  - no-referrer-when-downgrade _会共享完整的 URL_，因此并不能增强隐私。
  - strict-origin-when-cross-origin 和 strict-origin _只共享域_，
  - 而 no-referrer _完全不共享任何信息_。
  - 因此可以将 strict-origin-when-cross-origin、strict-origin 和 no-referrer 作为隐私增强的选项。
- **有用**
  - no-referrer 和 strict-origin _永远不会共享完整的 URL，即使对于同域请求也不例外，_
  - 所以如果此有需求，那么 strict-origin-when-cross-origin 是更好的选择。

**信任令牌 (Trust Token)**

信任令牌是一种新 API。利用此 API，网站可以将有限数量的信息从一个浏览上下文传送到另一个上下文（例如，跨站），这样，无需被动跟踪即可防止欺诈。

利用信任令牌，来源能够向信任的用户颁发加密令牌。用户浏览器会存储令牌。随后，浏览器可以在其他上下文中使用令牌来评估用户的真实性。

利用信任令牌 API 可以将用户在一个上下文中的信任传递到另一个上下文中，而无需识别用户或关联两个身份。

**通过 User-Agent Client Hints API 改善用户隐私和开发者体验**

用户代理客户端提示[(User-Agent Client Hints API](https://developer.mozilla.org/en-US/docs/Web/API/User-Agent_Client_Hints_API)扩展了[Client Hints](https://developer.mozilla.org/en-US/docs/Web/HTTP/Client_hints) 以提供一种通过 User-Agent 响应和请求标头以及 JavaScript API 公开浏览器和平台信息的方法。

目前算是实验性质，高版本的 Chromium 系的浏览器支持，但 Firefox、safari 等还不支持

解析 `User-Agent` 字符串一直是获取有关用户浏览器或设备信息的方法。  
`用户代理客户端提示`旨在通过强制执行服务器请求一组信息的模型，以更保护隐私的方式提供此信息。  
浏览器决定返回什么。这种方法意味着用户代理可以提供**允许用户隐藏一些可以从此类请求中识别出他们的信息的设置**。

通过这个 API 访问的信息被分成两组——低熵和高熵提示。
**低熵(low entropy)提示**是那些*不会泄露太多信息*的提示，API 使每个请求都可以轻松访问这些提示。
**高熵(high entropy)提示**有*可能泄露更多信息*，因此以浏览器可以决定是否提供它们的方式进行门控。

例如在 chrome 控制台打印:

```js
// 获得低熵提示
console.log(navigator.userAgentData.brands);
// [
//   { brand: "Google Chrome", version: "107" },
//   { brand: "Chromium", version: "107" },
//   { brand: "Not=A?Brand", version: "24" },
// ];
// 获得高熵提示
navigator.userAgentData
  .getHighEntropyValues([
    "architecture",
    "model",
    "platform",
    "platformVersion",
    "fullVersionList",
  ])
  .then((ua) => {
    console.log(ua);
  });
```

[用户代理 (UA) 客户端提示标头](https://developer.mozilla.org/en-US/docs/Web/HTTP/Client_hints#user-agent_client_hints)允许服务器根据用户代理（浏览器）、操作系统和设备来改变响应。标题包括：Sec-CH-UA, Sec-CH-UA-Arch, Sec-CH-UA-Bitness, Sec-CH-UA-Full-Version-List, Sec-CH-UA-Full-Version, Sec-CH-UA-Mobile, Sec-CH-UA-Model, Sec-CH-UA-Platform, 和 Sec-CH-UA-Platform-Version.

## MDN 的 web 安全概述

- 内容安全
  - [CSP (内容安全策略)](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/CSP)
- 连接安全
  - [传输层安全（TLS）](https://developer.mozilla.org/zh-CN/docs/Web/Security/Transport_Layer_Security)
  - HTTPS
  - [HTTP Strict-Transport-Security](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Headers/Strict-Transport-Security)
  - [证书透明度(HTTP Public Key Pinning (HPKP))](https://developer.mozilla.org/zh-CN/docs/Web/Security/Certificate_Transparency)
  - [混合内容(mixed content)](https://developer.mozilla.org/en-US/docs/Web/Security/Mixed_content)
  - [如何修复含有混合内容的网站](https://developer.mozilla.org/en-US/docs/Web/Security/Mixed_content/How_to_fix_website_with_mixed_content)
  - [安全上下文(SecureContext)](https://developer.mozilla.org/zh-CN/docs/Web/Security/Secure_Contexts)
  - [限制在安全上下文中的特性](https://developer.mozilla.org/en-US/docs/Web/Security/Secure_Contexts/features_restricted_to_secure_contexts)
  - [弱签名算法](https://developer.mozilla.org/zh-CN/docs/Web/Security/Weak_Signature_Algorithm)
- 数据安全
  - [使用 HTTP Cookies](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Cookies)
  - [Local Storage](https://developer.mozilla.org/zh-CN/docs/Web/API/Window/localStorage)
- 信息泄露
  - [Referer 标头策略：隐私和安全性考虑](https://developer.mozilla.org/en-US/docs/Web/Security/Referer_header:_privacy_and_security_concerns)
- 完整性
  - [同源策略(Same-origin policy)](https://developer.mozilla.org/zh-CN/docs/Web/Security/Same-origin_policy)
  - [子资源完整性(Subresource Integrity,SRI)](https://developer.mozilla.org/zh-CN/docs/Web/Security/Subresource_Integrity)
  - [`Access-Control-Allow-Origin`响应头](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Headers/Access-Control-Allow-Origin)
  - [`X-Content-Type-Options`响应头](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Headers/X-Content-Type-Options)
- 点击劫持保护
  - [`X-Frame-Options`响应头](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Headers/X-Frame-Options)
  - [CSP 指令:frame-ancestors](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Headers/Content-Security-Policy/frame-ancestors)
- 用户信息安全
  - [不安全的密码](https://developer.mozilla.org/en-US/docs/Web/Security/Insecure_passwords)
  - [隐私性和 :visited 选择器](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Privacy_and_the_:visited_selector)

## 常见的 web 攻击方式

根据[Web Security Academy](https://portswigger.net/web-security/learning-path)的 learning path，指定了一条方便学习的路线(由简到难)。分别为:

Server-side topics

- 1 SQL injection(用户输入了 SQL 指令字符串，程序没有检查，则可能在数据库服务器被认为正常指令而遭到破坏)
- 2 Authentication(身份验证机制很弱或者实现中的逻辑缺陷或糟糕的编码，使得攻击者完全绕过了身份验证机制(账密太简单也算))
- 3 Directory traversal(允许攻击者读取运行应用程序的服务器上的任意文件,比如对 url 中目录层级没有限制或者直接`../../xx`)
- 4 OS command injection(允许攻击者在运行应用程序的服务器上执行任意操作系统命令，如把用户输入值直接用作 shell 执行参数)
- 5 Business logic vulnerabilities(应用程序设计和实现中的缺陷使攻击者能够操纵合法功能以实现恶意目标,如[必填值未被真有填](https://portswigger.net/web-security/logic-flaws/examples))
- 6 [Information disclosure](https://portswigger.net/web-security/information-disclosure)(网站无意中向用户泄露敏感信息，比如在源代码中硬编码 API 密钥、IP 地址、数据库凭证等)
- 7 [Access control](https://portswigger.net/web-security/access-control)(用户实际上可以访问某些资源或执行某些他们不应该能够访问的操作，如控制访问的设计不完备)
- 8 File upload vulnerabilities(服务器未正确验证文件属性(类型、内容等)，文件成功上传后未受限制。如上传了启用远程代码的脚本)
- 9 [Server-side request forgery (SSRF)](https://portswigger.net/web-security/ssrf)(允许攻击者诱导服务器端应用向一个非预期的位置发出请求。内网的防御不那么强)
- 10 [XXE injection](https://portswigger.net/web-security/xxe)(允许攻击者干扰应用程序对`XML`数据的处理。因为`XML`规范包含各种潜在的危险特性，标准解析器支持这些特性)

Client-side topics

- 11 Cross-site scripting (XSS)(攻击者通过在目标网站上注入恶意脚本，使之在用户的浏览器上运行。)
- 12 [Cross-site request forgery (CSRF)](https://portswigger.net/web-security/csrf)(允许攻击者诱导用户执行他们不打算执行的操作。例如[2007 年 Gmail 的 CSRF 漏洞](https://www.davidairey.com/google-gmail-security-hijack/))
- 13 [Cross-origin resource sharing (CORS)](https://portswigger.net/web-security/cors)(网站的 CORS 策略配置和实施不当。例如 ACAO 响应头配置不当引发跨域攻击)
- 14 Clickjacking(通过点击诱饵网站中的其他内容，诱骗用户点击隐藏网站上的可操作内容)
- 15 [DOM-based vulnerabilities](https://portswigger.net/web-security/dom-based)(当网站包含的 js 将一个攻击者可控制的值传递给一个危险的函数时，会出现基于 DOM 的漏洞)
- 16 [WebSockets](https://portswigger.net/web-security/websockets)(几乎所有在普通 HTTP 中出现的网络安全漏洞都可以在 WebSockets 通信中出现)

Advanced topics

- 17 [Insecure deserialization](https://owasp.org/www-project-top-ten/2017/A8_2017-Insecure_Deserialization)(指用户可控制的数据被网站反序列化。攻击者修改了序列化对象，以便将有害数据传入应用程序代码。)
- 18 [Server-side template injection](https://portswigger.net/web-security/server-side-template-injection)(攻击者能够使用本机模板语法将恶意负载注入模板，然后在服务器端执行。)
- 19 Web cache poisoning(利用 Web 服务器和缓存的行为，从而将有害的 HTTP 响应提供给其他用户。)
- 20 [HTTP Host header attacks](https://portswigger.net/web-security/host-header)(该漏洞通常是由于有缺陷的假设:该头不是用户可控的。host 标头会创建隐式信任导致验证不充分)
- 21 [HTTP request smuggling](https://portswigger.net/web-security/request-smuggling)(一种干扰网站处理来自一个或多个用户的`HTTP`请求序列的技术。因为可在`HTTP`请求使用分块编码)
- 22 OAuth authentication(OAuth 规范在设计上相对模糊和灵活，绝大多数实现都是完全可选的)
- 23 JWT attacks(涉及用户向服务器发送修改后的`jwt`以实现恶意目标。因为`jwt`的实现缺陷，模拟已经通过验证的用户来绕过认证)

参看[OWASP Top 10:2021](https://owasp.org/Top10/zh_CN/A01_2021-Broken_Access_Control/)

### XSS

**是什么？**

跨站脚本（也被称为 XSS）是一个网络安全漏洞，它**允许攻击者破坏用户与易受攻击的应用程序的互动**。  
它允许攻击者规避同源策略(该策略旨在将不同的网站相互隔离开来)。  
跨站脚本漏洞通常允许攻击者伪装成受害者用户，执行用户能够执行的任何行动，并访问用户的任何数据。  
如果受害者用户在应用程序中拥有特权访问权，那么攻击者就可能获得对应用程序所有功能和数据的完全控制。

**如何工作？**

跨站脚本的工作原理是操纵一个有漏洞的网站，使其向用户返回恶意的 JavaScript。
当恶意代码在受害者的浏览器中执行时，攻击者可以完全破坏他们与应用程序的互动。

**有哪些类型？**

- Reflected XSS，恶意脚本来自于当前的 HTTP 请求。
- Stored XSS，恶意脚本来自网站的数据库。
- DOM-based XSS，即漏洞存在于客户端代码而非服务器端代码。

**Reflected XSS(反射型 XSS)**

反射式 XSS 是最简单的跨站脚本攻击。当一个应用程序接收 HTTP 请求中的数据，并**以不安全的方式将该数据包含在即时响应中时**，就会出现这种情况。

示例

响应把请求的参数数据解析后未做处理当成结果返回，而前端渲染数据时未对值进行处理直接渲染:

```txt
https://insecure-website.com/status?message=All+is+well.
<p>Status: All is well.</p>
```

该应用程序不会对数据进行任何其他处理，因此攻击者可以把参数的值改为恶意脚本，因为前后端都未处理，则会直接渲染该脚本：

```txt
https://insecure-website.com/status?message=<script>/*+Bad+stuff+here...+*/</script>
<p>Status: <script>/* Bad stuff here... */</script></p>
```

如果用户访问攻击者构建的 URL，则攻击者的脚本会在用户的浏览器中执行，在该用户与应用程序的会话上下文中。此时，脚本可以执行任何操作，并检索用户有权访问的任何数据。

**Stored XSS(储存型 XSS)**

当一个应用程序**从一个不受信任的来源接收数据，并以不安全的方式将该数据包含在其后来的 HTTP 响应中时**，就会出现存储的 XSS（也被称为持久性或二阶 XSS）。

有问题的数据可能是通过 HTTP 请求提交给应用程序的；例如，博客文章的评论，聊天室的用户昵称，或客户订单的联系信息。
在其他情况下，数据可能来自其他不可信的来源；例如，显示通过 SMTP 收到的信息的网络邮件应用程序，显示社交媒体帖子的营销应用程序，或显示网络流量数据的网络监控应用程序。

示例

一个留言板应用程序让用户提交信息，其他用户在查看留言板时可以显示该用户的提交:

```txt
<p>Hello, this is my message!</p>
```

该应用程序不对数据进行任何其他处理，因此攻击者可以轻易地发送攻击其他用户的信息:

```txt
<p><script>/* Bad stuff here... */</script></p>
```

**DOM-based XSS(基于 DOM 的 XSS)**

DOM-based XSS 产生于一个应用程序包含一些客户端的 JavaScript，以*不安全的方式处理来自不受信任的来源的数据*，通常是通过将数据写回 DOM。

示例

一个应用程序使用一些 JavaScript 来读取一个输入字段的值，并将该值写入 HTML 中的一个元素。

```txt
var search = document.getElementById('search').value;
var results = document.getElementById('results');
results.innerHTML = 'You searched for: ' + search;
```

如果攻击者能够控制输入字段的值，他们可以很容易地构建一个恶意的值，导致自己的脚本执行。

```txt
You searched for: <img src=1 onerror='/* Bad stuff here... */'>
```

**XSS 的用途**

利用跨站脚本漏洞的攻击者通常能够:

- 冒充或伪装成受害者用户。
- 执行用户能够执行的任何行动。
- 读取用户能够访问的任何数据。
- 捕获用户的登录凭证。
- 对网站进行虚拟污损。
- 在网站中注入木马功能。

**XSS 漏洞的影响**

XSS 攻击的实际影响一般取决于应用程序的性质、其功能和数据以及被攻击用户的状态。比如说。

- 在一个宣传册软件的应用中，所有的用户都是匿名的，所有的信息都是公开的，其影响往往是最小的。
- 在一个拥有敏感数据的应用程序中，如银行交易、电子邮件或医疗记录，其影响通常会很严重。
- 如果被攻击的用户在应用程序中拥有较高的权限，那么影响通常会很严重，允许攻击者完全控制有漏洞的应用程序，并危及所有用户和他们的数据。

**如何防止**
一般来说，有效防止 XSS 漏洞可能涉及以下措施的组合：

- **到达时过滤输入(Filter input on arrival)**。在接收到用户输入时，尽可能严格地根据预期或有效输入进行过滤。
- **在输出上编码数据(Encode data on output)**。在 HTTP 响应中输出用户可控数据时，对输出进行编码以防止其被解释为活动内容。根据输出上下文，这可能需要应用 HTML、URL、JavaScript 和 CSS 编码的组合。
- **使用适当的响应标头(Use appropriate response headers)**。为了防止 HTTP 响应中不包含任何 HTML 或 JavaScript 的 XSS，您可以使用 `Content-Type` 和 `X-Content-Type-Options` 标头来确保浏览器以您想要的方式解释响应。
- **内容安全政策(CSP)**。作为最后一道防线，您可以使用内容安全策略 (CSP) 来降低仍然发生的任何 XSS 漏洞的严重性。

### CSRF

**是什么？**

跨站请求伪造（也称为 CSRF）是一个网络安全漏洞，**允许攻击者诱导用户执行他们不打算执行的操作**。它允许攻击者部分规避同源策略(该策略旨在防止不同网站相互干扰)。

**影响是什么？**

在成功的 CSRF 攻击中，攻击者*会导致受害者用户无意中执行某项操作*。  
例如，这可能是更改其帐户上的电子邮件地址、更改密码或进行资金转账。根据操作的性质，攻击者可能能够完全控制用户的帐户。  
如果受感染的用户在应用程序中拥有特权角色，那么攻击者可能能够完全控制应用程序的所有数据和功能。

**如何工作?**

要使 CSRF 攻击成为可能，必须具备三个关键条件：

- **一个相关的动作**。应用程序中存在攻击者有理由诱导的操作。这可能是特权操作（例如修改其他用户的权限）或对用户特定数据的任何操作（例如更改用户自己的密码）。
- **基于 Cookie 的会话处理**。执行该操作涉及发出一个或多个 HTTP 请求，并且应用程序仅依赖会话 cookie 来识别发出请求的用户。没有其他机制可用于跟踪会话或验证用户请求。
- **没有不可预测的请求参数**。执行该操作的请求不包含攻击者无法确定或猜测其值的任何参数。例如，当导致用户更改密码时，如果攻击者需要知道现有密码的值，则该功能不会受到攻击。

**典型流程**

一个典型的 CSRF 攻击有着如下的流程：

- 受害者登录`a.com`，并保留了登录凭证（Cookie）。
- 攻击者引诱受害者访问了`b.com`(比如中奖信息的链接跳转，里面是恶意操作)。
- `b.com` 向 `a.com` 发送了一个请求：`a.com/act=xx`。浏览器会默认携带`a.com`的 Cookie。
- `a.com`接收到请求后，对请求进行验证，并确认是受害者的凭证，误以为是受害者自己发送的请求。
- `a.com`以受害者的名义执行了`act=xx`。
- 攻击完成，攻击者在受害者不知情的情况下，冒充受害者，让`a.com`执行了自己定义的操作。

**示例**

在 gmail 中看到一个大甩卖的信息，点击链接一看是空白的，很失望。但后来发现自己的邮件泄露，造成了严重问题。

原来空白的链接中有嵌入恶意代码，这个页面只要打开，就会向 Gmail 发送一个 post 请求。请求中，执行了“Create Filter”命令，将所有的邮件，转发到“hacker@hackermail.com”。

因为先登录了 gmail，虽有有了 cookie，在点开大甩卖页面时，该页面向 gmail 发送的 post 请求中会带上该 cookie，gmail 服务器不知道是大甩卖页面发送的请求，以为还是正常用户，就执行了邮件转发的设置。造成了邮件泄露。

**防止 CSRF 攻击**

- CSRF 自动防御策略：同源检测（Origin 和 Referer 验证）。
- CSRF 主动防御措施：Token 验证 或者 双重 Cookie 验证 以及配合 Samesite Cookie。
  - 防御 CSRF 攻击的最可靠方法是在相关请求中包含[CSRF Token](https://portswigger.net/web-security/csrf/tokens)。令牌应该是：
    - 对于一般的会话令牌，高熵是不可预测的。
    - 绑定到用户的会话。
    - 在执行相关操作之前，在每种情况下都经过严格验证。
- 保证页面的幂等性，后端接口不要在 GET 页面中做用户操作。

对 CSRF 攻击的保护通常是通过使用 CSRF 令牌来实现的：一个针对会话的、一次性使用的数字或 nonce。CSRF 令牌被置于请求中，并作为正常行为会话的一部分传递给服务器。

### 由 CORS 配置问题引起的漏洞

许多现代网站使用 CORS 来允许来自子域和受信任的第三方的访问。他们的 CORS 实现可能包含错误或过于宽松以确保一切正常，这可能导致可利用的漏洞。

- **服务器生成的 ACAO 头来自客户指定的 Origin 头**
  - 请求端的`Origin`头是恶意网站，如果服务端配置`Access-Control-Allow-Origin`头(简称 ACAO)来自该值，则容易被攻击
- **解析 Origin 头文件的错误**
  - 有些允许子域访问的配置，ACAO 的值会局部匹配`Origin`头，如果恶意网站也是局部匹配该头，则会被被信任跨域操作
- **白名单上 Origin 的 null 值**
  - Origin 标头的规范支持 null 值。浏览器可能会在各种异常情况下发送 Origin 标头中的 null 值：
    - 跨域重定向。来自序列化数据的请求。请求使用`file:`协议。沙盒化的跨域请求。
  - 攻击者可以使用各种技巧来生成包含 Origin 标头 null 中的值的跨域请求。满足白名单，又实现了跨域请求。
- **通过 CORS 的信任关系利用 XSS**
  - 就算是正确的 CORS 配置也是两个源之间建立信任关系。如果其中一个源是易被 XSS 攻击的源，那可以利用 CORS 获取另一个源的敏感信息
- **用配置不当的 CORS 破坏 TLS**
  - 假设一个严格采用 HTTPS 的应用程序也将一个使用普通 HTTP 的可信子域列入白名单。
- **内网和 CORS 没有凭证**(Intranets and CORS without credentials)
  - 大多数 CORS 攻击依赖于响应标头 ACAC 的存在：`Access-Control-Allow-Credentials: true`
    - 如果没有该标头，受害者用户的浏览器将拒绝发送他们的 cookie
  - 但内网的安全标准通常低于外部网站，从而使攻击者能够发现漏洞并获得进一步的访问权限。比如`ACAO`是通配\*,则没有`ACAC`头
    - 如果私有 IP 地址空间内的用户访问公共互联网，则可以从外部站点执行基于 CORS 的攻击，该外部站点使用受害者的浏览器作为访问内部网资源的代理。

**防止 CORS-based attacks**

- **正确配置跨来源请求**: 应该在`Access-Control-Allow-Origin`头中正确指定来源。
- **只允许信任的网站**: ACAO 头配置时，尤其注意动态配置来自`Origin`请求头值的设计。
- **避免白名单上的 null**:任何源都可以用 null 源创建一个恶意文件。因此，应该避免将 ACAO 标头设置为‘null’值。
- **避免在内部网络中使用通配符**:当内部浏览器可以访问不受信任的外部域时，仅仅相信网络配置来保护内部资源是不够的。
- **CORS 不能替代服务端的安全策略**:CORS 定义了浏览器的行为,除了正确配置 CORS 外，服务端应该继续对敏感信息进行保护，例如认证、会话管理等。

### Clickjacking

**是什么？**

点击劫持是一种基于界面的攻击，即**通过点击诱饵网站中的一些其他内容来诱使用户点击隐藏网站中的可操作内容。**，透明度为 0 的 banner 嵌入恶意代码。

示例

一个网络用户访问了一个诱饵网站（也许这是一个由电子邮件提供的链接），并点击了一个按钮来赢取奖品。
在不知情的情况下，他们被攻击者欺骗，按了另一个隐藏的按钮，结果是在另一个网站上支付了一个账户。这是一个点击劫持攻击的例子。

这种技术取决于将一个看不见的、可操作的网页（或多个网页）纳入其中，其中包含一个按钮或隐藏链接，例如，在一个 iframe 中。
该 iframe 被覆盖在用户预期的诱饵网页内容之上。

_这种攻击与 CSRF 攻击的不同之处在于，用户需要执行一个动作，如点击按钮，而 CSRF 攻击则取决于在用户不知道或不输入的情况下伪造整个请求。_

**点击劫持和 XSS 的组合**

当点击劫持被用作另一种攻击（如 DOM XSS 攻击）的载体时，它的真正威力就显现出来了。
假设攻击者首先确定了 XSS 攻击，那么这种联合攻击的实施就相对简单了。
然后将 XSS 攻击与 iframe 目标 URL 相结合，使用户点击按钮或链接，从而执行 DOM XSS 攻击。

**防止点击劫持**

只要网站可以被框住(framed)，点击劫持攻击就有可能。因此，预防技术的基础是限制网站的框架能力。通过网络浏览器进行的常见客户端保护是使用框架破坏(frame busting)或框架破坏脚本(frame breaking scripts)。脚本的行为:

- 检查并强制执行当前应用程序窗口是主窗口或顶层窗口。
- 使所有框架可见。
- 防止点击不可见的框架。
- 拦截并向用户提示潜在的点击劫持攻击。

但是，它们通常可以被攻击者规避。

- 因为是 js 脚本，所以可能会被浏览器的安全设置所阻止执行，甚至浏览器不支持 js 脚本
- 攻击者可以使用 html5 的 iframe 标签的`sandbox`属性。当该属性被设置为 allow-forms 或 allow-scripts 值，并省略 allow-top-navigation 值时，框架破坏者脚本就可以被消灭，因为 iframe 无法检查它是否是顶部窗口。

点击劫持是一种浏览器端行为，其成功与否取决于浏览器的功能和对现行网络标准和最佳实践的遵守情况。
服务器端对点击劫持的保护是通过定义和交流对组件（如 iframe）使用的限制来实现的。
然而，保护的实施取决于浏览器对这些约束的遵守和执行。服务器端点击劫持保护的两个机制是`X-Frame-Options`和内容安全策略(CSP)。

- HTTP CSP 标头指定可以包含`<iframe>`等标签的源:
  - `Content-Security-Policy:frame-ancestors <source> <source>;`
- 使用`X-Frame-Options`标头给浏览器指示是否允许一个页面展示`<frame>`、`<iframe>`、`<embed>`或者`<object>`中的标记。

### 基于 DOM 的漏洞

基于 DOM 的漏洞(DOM-based vulnerabilities)

**什么是 DOM？**
文档对象模型 (DOM) 是 web 浏览器对页面元素的分层表示。网站可以使用 JavaScript 来操作 DOM 的节点和对象，以及它们的属性。  
DOM 操作本身不是问题。事实上，它是现代网站运作方式不可或缺的一部分。但是，不安全地处理数据的 JavaScript 可能会引发各种攻击。  
**当网站包含的 JavaScript 获取攻击者可控制的值（称为源）并将其传递给危险函数（称为接收器）时**，就会出现基于 DOM 的漏洞。

**污染流漏洞(Taint-flow vulnerabilities)**

许多基于 DOM 的漏洞可以追溯到客户端代码操作攻击者可控数据的方式问题。

首先了解 `源(sources)` 和 `接收器(sinks)` 之间污染流(taint flow)的基本知识。

**源**是一个 _JavaScript 属性，它接受可能受攻击者控制的数据。_

- 一个源的例子是`location.search`属性，因为它从查询字符串中读取输入，这对攻击者来说是相对简单的控制。
- 最终，任何可以被攻击者控制的属性都是一个潜在的来源。
- 这包括引用的 URL（由 document.referrer 字符串暴露），用户的 cookies（由 document.cookie 字符串暴露），和网络信息。

**接收器**是一个*潜在的危险 JavaScript 函数或 DOM 对象，如果攻击者控制的数据被传递给它，它可能会造成不良影响。*

- 例如，eval()函数是一个接收器，因为它处理作为 JavaScript 传递给它的参数。
- 一个 HTML 接收器的例子是 document.body.innerHTML，因为它有可能允许攻击者注入恶意的 HTML 并执行任意的 JavaScript。

_根本上讲，当网站将数据从源传递到接收器时，会出现基于 DOM 的漏洞，然后接收器在客户端会话的上下文中以不安全的方式处理数据。_

**示例**

_最常见的源是 URL，通常使用`location`对象访问该 URL。_

攻击者可以构造一个链接，将受害者发送到一个有漏洞的页面，该页面的查询字符串和 URL 的片段部分中包含有效载荷。

如果业务逻辑中，有对`location`对象做类似处理:

```js
goto = location.hash.slice(1);
if (goto.startsWith("https:")) {
  location = goto;
}
```

攻击者可能构建一个`https://www.innocent-website.com/example#https://www.evil-user.net`这样的 url，那么`location`对象取值到了
`https://www.evil-user.net`，最后用户可能就访问了该钓鱼网站之类的。

**常见的源**

以下是可用于利用各种污点流漏洞的典型源:

```
document.URL
document.documentURI
document.URLUnencoded
document.baseURI
location
document.cookie
document.referrer
window.name
history.pushState
history.replaceState
localStorage
sessionStorage
IndexedDB (mozIndexedDB, webkitIndexedDB, msIndexedDB)
Database
```

此外还有[反射型数据、储存型数据](https://portswigger.net/web-security/cross-site-scripting/dom-based#dom-xss-combined-with-reflected-and-stored-data)、[web 的 message](https://portswigger.net/web-security/dom-based/controlling-the-web-message-source)也可能作为污点流漏洞的源。

反射型数据例如一个查询条件的值，传到后台，又响应传回前台，进行了渲染(注意反射型 XSS)

储存型数据例如一条文章评论，存入了数据库，其他人再查看文档时，从数据库取得显示在评论区(注意存储型 XSS)

**可能导致基于 DOM 漏洞的接收器**

| DOM-based vulnerability          | Example sink             | DOM-based vulnerability     | Example sink        |
| -------------------------------- | ------------------------ | --------------------------- | ------------------- |
| DOM XSS                          | document.write()         | JavaScript injection        | eval()              |
| Open redirection                 | window.location          | WebSocket-URL poisoning     | WebSocket()         |
| Cookie manipulation              | document.cookie          | Link manipulation           | element.src         |
| Document-domain manipulation     | document.domain          | Denial of service           | RegExp()            |
| Ajax request-header manipulation | setRequestHeader()       | Web message manipulation    | postMessage()       |
| Local file-path manipulation     | FileReader.readAsText()  | Client-side SQL injection   | ExecuteSql()        |
| HTML5-storage manipulation       | sessionStorage.setItem() | Client-side JSON injection  | JSON.parse()        |
| DOM-data manipulation            | element.setAttribute()   | Client-side XPath injection | document.evaluate() |

**如何防止基于 DOM 的污点流漏洞**

没有一个单一的行动可以让你完全消除基于 DOM 的攻击的威胁。
然而，一般来说，避免基于 DOM 的漏洞的最有效方法是**避免允许来自任何不受信任的源的数据动态更改传输到任何接收器的值**。

the most effective way to avoid DOM-based vulnerabilities is to avoid allowing data from any untrusted source to dynamically alter the value that is transmitted to any sink.

如果应用程序所需的功能意味着这种行为是不可避免的，那么必须在客户端的代码中实现防御措施。  
在许多情况下，相关数据可以在白名单的基础上进行验证，只允许已知是安全的内容。  
在其他情况下，将有必要对数据进行消毒或编码。  
这可能是一项复杂的任务，根据数据插入的环境，可能涉及到 JavaScript 转义、HTML 编码和 URL 编码的组合，以适当的顺序进行。

确保实施强有力的措施来验证任何传入消息的来源。

### WebSockets 安全漏洞

原则上，几乎所有与 WebSocket 相关的 Web 安全漏洞都可能出现：

- 传输到服务器的用户提供的输入可能会以不安全的方式进行处理，从而导致 SQL 注入或 XML 外部实体注入等漏洞。
- 通过 WebSockets 达到的一些盲漏洞可能只能使用带外 (OAST) 技术检测到。
- 如果攻击者控制的数据通过 WebSockets 传输给其他应用程序用户，则可能导致 XSS 或其他客户端漏洞。

**操纵 WebSocket 流量**

- 拦截和修改 WebSocket 消息(Intercept and modify WebSocket messages.)
  - 如果没有其他输入处理或防御在起作用，攻击者可以通过提交以下 WebSocket 消息来执行概念验证 XSS 攻击(消息中嵌恶意脚本)
- 重放和生成新的 WebSocket 消息(Replay and generate new WebSocket messages.)
- 操作 WebSocket 连接(Manipulate WebSocket connections.)
  - 一些 WebSockets 漏洞只能通过操纵 WebSocket 握手来发现和利用。这些漏洞往往涉及设计缺陷，
    - 错误地信任 HTTP 标头以执行安全决策，例如 X-Forwarded-For 标头。
    - 会话处理机制的缺陷，因为处理 WebSocket 消息的会话上下文通常由握手消息的会话上下文决定。
    - 应用程序使用的自定义 HTTP 标头引入的攻击面。
  - 当攻击者从攻击者控制的网站建立跨域 WebSocket 连接时，就会出现一些 WebSocket 安全漏洞。
    - 这被称为跨站点 WebSocket 劫持攻击，它涉及利用 WebSocket 握手上的跨站点请求伪造( CSRF ) 漏洞。
    - 攻击通常会产生严重影响，允许攻击者代表受害用户执行特权操作或捕获受害用户可以访问的敏感数据。

**如何保护 WebSocket 连接**

- 使用`wss://`协议（基于 TLS 的 WebSockets）。
- 对 WebSockets 端点的 URL 进行硬编码，当然不会将用户可控制的数据合并到该 URL 中。
- 保护 WebSocket 握手消息免受 CSRF 攻击，避免跨站 WebSockets 劫持漏洞。
- 将通过 WebSocket 接收的数据在两个方向上都视为不受信任。
  - 在服务器端和客户端安全地处理数据，以防止基于输入的漏洞，例如 SQL 注入和跨站点脚本。

### SQLi(SQL 注入)

SQL 注入 (SQLi) 是一种网络安全漏洞，允许攻击者干扰应用程序对其数据库的查询。  
它通常允许攻击者查看他们通常无法检索的数据。这可能包括属于其他用户的数据，或应用程序本身能够访问的任何其他数据。  
在许多情况下，攻击者可以修改或删除这些数据，从而导致应用程序的内容或行为发生持续变化。  
在某些情况下，攻击者可以升级 SQL 注入攻击以破坏底层服务器或其他后端基础架构，或执行拒绝服务攻击。

**如何防止 SQL 注入**

大多数 SQL 注入实例可以通过**使用参数化查询（也称为预准备语句,prepared statements）**而不是查询中的字符串连接来防止。

为了使参数化查询有效地防止 SQL 注入，**查询中使用的字符串必须始终是硬编码的常量**，并且不得包含来自任何来源的任何可变数据。

- 严格限制 Web 应用的数据库的操作权限
- 后端代码检查输入的数据是否符合预期
- 对进入数据库的特殊字符（'，"，\，<，>，&，\*，; 等）进行转义处理，或编码转换。
- 所有的查询语句建议使用数据库提供的参数化查询接口

### OS 命令注入攻击

OS 命令注入和 SQL 注入差不多，只不过 SQL 注入是针对数据库的，而 OS 命令注入是针对操作系统的。  
OS 命令注入攻击指通过 Web 应用，执行非法的操作系统命令达到攻击的目的。  
只要在能调用 Shell 函数的地方就有存在被攻击的风险。倘若调用 Shell 时存在疏漏，就可以执行插入的非法命令。  
命令注入攻击可以向 Shell 发送命令，让 Windows 或 Linux 操作系统的命令行启动程序。  
也就是说，通过命令注入攻击可执行操作系统上安装着的各种程序。

**如何防御**

防止操作系统命令注入漏洞的最有效方法是**永远不要从应用层代码调用操作系统命令**。几乎在每种情况下，都存在使用更安全的平台 API 实现所需功能的替代方法。

- 后端对前端提交内容进行规则限制（比如正则表达式）。
- 在调用系统命令前对所有传入参数进行命令行参数转义过滤。
- 不要直接拼接命令语句，借助一些工具做拼接、转义预处理，例如 Node.js 的 shell-escape npm 包

如果认为*使用用户提供的输入调用操作系统命令是不可避免*的，则**必须执行强输入验证**。有效验证的一些示例包括：

- 根据允许值的白名单进行验证。
- 验证输入是否为数字。
- 验证输入仅包含字母数字字符，不包含其他语法或空格。

永远不要试图通过转义 shell 元字符来清理输入。在实践中，这太容易出错并且容易被熟练的攻击者绕过。
