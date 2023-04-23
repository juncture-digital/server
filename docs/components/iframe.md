# ve-iframe

<style> 
    .markdown-section h3 ~ p > strong > a { color: crimson; font-size: 110%; text-decoration: none; }
    .markdown-section table { 
        margin-left:3rem; 
        width: calc(100% - 6rem); 
        border:1px solid #555;
    }
    .markdown-section td, .markdown-section th {
        border:1px solid #555;
        padding: 8px;
        line-height: 1.2;
    }
    .markdown-section th {
        background-color:#E2F0F7;
        font-weight:bold !important;
        text-align:center !important;
    }
</style>

The `.ve-iframe` tag allows arbitrary web pages to be embedded in an essay.  The tag is a light wrapper around the standard HTML [iframe](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe) tag that is used to embed another document within the current HTML document.

## Attributes

### Basic attributes

**[src](#basic)** (_string_):  The URL of the page to embed. Use a value of about:blank to embed an empty page that conforms to the [same-origin policy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy#inherited_origins). Also note that programmatically removing an iframe's src attribute (e.g. via [Element.removeAttribute()](https://developer.mozilla.org/en-US/docs/Web/API/Element/removeAttribute)) causes about:blank to be loaded in the frame in Firefox (from version 65), Chromium-based browsers, and Safari/iOS.

### Viewer positioning attributes

**[left](/styling/viewer-positioning)** (_boolean_):  Position the viewer in the left half of the viewport and scale the width proportionally.  Text will wrap around the viewer unless the _sticky_ attribute is included.

**[right](/styling/viewer-positioning)** (_boolean_):  Position the viewer in the right half of the viewport and scale the width proportionally. Text will wrap around the viewer unless the _sticky_ attribute is included.

**[full](/styling/viewer-positioning)** (_boolean_):  Use the fill width of the browser viewport for the image.  Scale the image height proportional to the source image.  By default, the image will be auto-sized such that its height is not more than 40% of the viewport height.

**[sticky](/styling/viewer-positioning)** (_boolean_):  The _sticky_ attribute causes the viewer to "stick" to the top of the viewing area when the essay text is scrolled.  The viewer will stick in position until all content in the enclosing section has scrolled through the viewing area.

**[height](/styling/viewer-positioning)** (_string_):  A requested size for the  viewer height.  The default behavior is to use the full width of the available window and scale the viewer height to retain the aspect ratio of the source item (image or video).

**[width](/styling/viewer-positioning)** (_string_):  A requested size for the  viewer width.  The default behavior is to use the full width of the available window.

### Expert attributes

The following attributes are passed through to the native `iframe` element.  These attributes should not normally be needed.

**[allow](#expert)** (_string_):  Specifies a [Permissions Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Permissions_Policy) for the iframe. The policy defines what features are available to the iframe (for example, access to the microphone, camera, battery, web-share, etc.) based on the origin of the request.

**[allowfullscreen](#expert)** (_boolean_):  Set to true if the **[allow](#expert)** (_string_):  Specifies a [Permissions Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Permissions_Policy) for the iframe. The policy defines what features are available to the iframe (for example, access to the microphone, camera, battery, web-share, etc.) based on the origin of the request.
 can activate fullscreen mode by calling the requestFullscreen() method.

**[credentialless](#expert)** (_string_):  Set to true to make the iframe credentialless, meaning that its content will be loaded in a new, ephemeral context. It doesn't have access to the network, cookies, and storage data associated with its origin. It uses a new context local to the top-level document lifetime. In return, the [Cross-Origin-Embedder-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cross-Origin-Embedder-Policy) (COEP) embedding rules can be lifted, so documents with COEP set can embed third-party documents that do not. See [IFrame credentialless](https://developer.mozilla.org/en-US/docs/Web/Security/IFrame_credentialless) for more details.

**[csp](#expert)** (_string_):  A [Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) enforced for the embedded resource. See [HTMLIFrameElement.csp](https://developer.mozilla.org/en-US/docs/Web/API/HTMLIFrameElement/csp) for details.

**[fetchpriority](#expert)** (_string_):  Provides a hint of the relative priority to use when fetching the iframe document. Allowed values:

| Value | Description |
| -------- | ---------------------------------------- |
| high | Signals a high-priority fetch relative to other iframe documents. |
| low  | Signals a low-priority fetch relative to other iframe documents. |
| auto | Default: Signals automatic determination of fetch priority relative to other iframe documents. |

**[loading](#expert)** (_string_):  Indicates how the browser should load the iframe:

| Value | Description |
| -------- | ---------------------------------------- |
| eager | Load the iframe immediately, regardless if it is outside the visible viewport (this is the default value) |
| lazy  | Defer loading of the iframe until it reaches a calculated distance from the viewport, as defined by the browser. |

**[name](#expert)** (_string_):  A targetable name for the embedded browsing context. This can be used in the target attribute of the `a`, `form`, or `base` elements; the formtarget attribute of the `input` or `button` elements; or the windowName parameter in the [window.open()](https://developer.mozilla.org/en-US/docs/Web/API/Window/open) method.

**[referrerpolicy](#expert)** (_string_):  Indicates which referrer to send when fetching the frame's resource:

| Value | Description |
| -------- | ---------------------------------------- |
| no-referrer                     | The [Referer](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer) header will not be sent. |
| no-referrer-when-downgrade      | The [Referer](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer) header will not be sent to [origins](https://developer.mozilla.org/en-US/docs/Glossary/Origin) without [TLS](https://developer.mozilla.org/en-US/docs/Glossary/TLS) ([HTTPS](https://developer.mozilla.org/en-US/docs/Glossary/HTTPS)). |
| origin                          | The sent referrer will be limited to the origin of the referring page: its [scheme](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_URL), [host](https://developer.mozilla.org/en-US/docs/Glossary/Host), and [port](https://developer.mozilla.org/en-US/docs/Glossary/Port). |
| origin-when-cross-origin        | The referrer sent to other origins will be limited to the scheme, the host, and the port. Navigations on the same origin will still include the path.
 |
| same-origin                     | A referrer will be sent for [same origin](https://developer.mozilla.org/en-US/docs/Glossary/Same-origin_policy), but cross-origin requests will contain no referrer information. |
| strict-origin                   | Only send the origin of the document as the referrer when the protocol security level stays the same (HTTPS→HTTPS), but don't send it to a less secure destination (HTTPS→HTTP). |
| strict-origin-when-cross-origin | (default): Send a full URL when performing a same-origin request, only send the origin when the protocol security level stays the same (HTTPS→HTTPS), and send no header to a less secure destination (HTTPS→HTTP). |
| unsafe-url                      | The referrer will include the origin and the path (but not the [fragment](https://developer.mozilla.org/en-US/docs/Web/API/HTMLAnchorElement/hash), [password](https://developer.mozilla.org/en-US/docs/Web/API/HTMLAnchorElement/password), or [username](https://developer.mozilla.org/en-US/docs/Web/API/HTMLAnchorElement/username)). This value is unsafe, because it leaks origins and paths from TLS-protected resources to insecure origins. |

**[sandbox](#expert)** (_string_):  Applies extra restrictions to the content in the frame. The value of the attribute can either be empty to apply all restrictions, or space-separated tokens to lift particular restrictions:

| Value | Description |
| -------- | ---------------------------------------- |
| allow-downloads-without-user-activation | Allows for downloads to occur without a gesture from the user. |
| allow-downloads | Allows for downloads to occur with a gesture from the user. |
| allow-forms | Allows the resource to submit forms. If this keyword is not used, form submission is blocked. |
| allow-modals | Lets the resource [open modal windows](https://html.spec.whatwg.org/multipage/browsers.html#sandboxed-modals-flag) |
| allow-orientation-lock | Lets the resource [lock the screen orientation](https://developer.mozilla.org/en-US/docs/Web/API/Screen/lockOrientation). |
| allow-pointer-lock | Lets the resource use the [Pointer Lock API.](https://developer.mozilla.org/en-US/docs/Web/API/Pointer_Lock_API) |
| allow-popups | Allows popups (such as window.open(), target="_blank", or showModalDialog()). If this keyword is not used, the popup will silently fail to open. |
| allow-popups-to-escape-sandbox | Lets the sandboxed document open new windows without those windows inheriting the sandboxing. For example, this can safely sandbox an advertisement without forcing the same restrictions upon the page the ad links to. |
| allow-presentation | Lets the resource start a [presentation session](https://developer.mozilla.org/en-US/docs/Web/API/PresentationRequest). |
| allow-same-origin | If this token is not used, the resource is treated as being from a special origin that always fails the [same-origin policy](https://developer.mozilla.org/en-US/docs/Glossary/Same-origin_policy) (potentially preventing access to [data storage/cookies](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy#cross-origin_data_storage_access) and some JavaScript APIs). |
| allow-scripts | Lets the resource run scripts (but not create popup windows). |
| allow-storage-access-by-user-activation | Lets the resource request access to the parent's storage capabilities with the [Storage Access API](https://developer.mozilla.org/en-US/docs/Web/API/Storage_Access_API). |
| allow-top-navigation | Lets the resource navigate the top-level browsing context (the one named _top). |
| allow-top-navigation-by-user-activation | Lets the resource navigate the top-level browsing context, but only if initiated by a user gesture. |

**[srcdoc](#expert)** (_string_):  Inline HTML to embed, overriding the src attribute. If a browser does not support the srcdoc attribute, it will fall back to the URL in the src attribute.

## Examples

### Basic

<ve-snippet collapsible label="Embedding a KnightLab Timeline">
.ve-iframe https://cdn.knightlab.com/libs/timeline3/latest/embed/index.html?source=1xuY4upIooEeszZ_lCmeNx24eSFWe0rHe9ZdqH2xqVNk&font=Default&lang=en&initial_zoom=2&height=100%
</ve-snippet>

<ve-snippet collapsible label="Embedding a KnightLab Timeline with right positioning">
.ve-iframe https://cdn.knightlab.com/libs/timeline3/latest/embed/index.html?source=1xuY4upIooEeszZ_lCmeNx24eSFWe0rHe9ZdqH2xqVNk&font=Default&lang=en&initial_zoom=2&height=100% right
</ve-snippet>

<ve-snippet collapsible label="Wikimedia Commons picture of the day">
.ve-iframe https://commons.wikimedia.org/wiki/Commons:Picture_of_the_day/Today
</ve-snippet>

<ve-snippet collapsible label="Embedding a Book from Internet Archive">
.ve-iframe https://archive.org/embed/slaveryinunit00ballcha/page/172/mode/1up
</ve-snippet>
