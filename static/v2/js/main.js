const junctureDomains = new Set(['juncture-digital.org', 'www.juncture-digital.org', 'beta.juncture-digital.org', 'dev.juncture-digital.org', 'editor.juncture-digital.org', 'visual-essays.net', 'localhost:8080', 'localhost:5555'])
const isJuncture = junctureDomains.has(location.host)
let PREFIX = window.PREFIX
let REF = window.REF
console.log(`PREFIX=${PREFIX} REF=${REF} host=${location.host} isJuncture=${isJuncture}`)

// Remove ref query argument from browser URL if same as REF
if (!isJuncture) {
  let re = new RegExp(`^\/${PREFIX}`)
  let browserPath = `${location.origin}${location.pathname.replace(re,'')}`
  let qargsRef = (new URL(document.location)).searchParams.get('ref')
  if (qargsRef && qargsRef !== REF) browserPath += `?ref=${qargsRef}`
  window.history.replaceState({}, document.title, browserPath)
}

window.isMobile = ('ontouchstart' in document.documentElement && /mobi/i.test(navigator.userAgent) )
window.isEditor = location.port === '5555' || location.hostname.indexOf('editor') == 0

document.body.classList.remove('hidden')
document.body.classList.add('visible')

// Google Analytics
window.dataLayer = window.dataLayer || []
function gtag(){dataLayer.push(arguments)}
gtag('js', new Date())
gtag('config', 'G-DRHNQSMN5Y')
