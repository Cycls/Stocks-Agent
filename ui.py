import urllib.parse

header = """
<raw>
<style>
  .sky {
    background: radial-gradient(
        1400px 500px at 50% -60%,
        rgba(255, 255, 255, 0.95),
        rgba(255, 255, 255, 0.5),
        rgba(255, 255, 255, 0) 75%
      ),
      linear-gradient(
        180deg,
        #ffb7b2 0%,
        #ffc0ac 15%,
        #ffd0b8 30%,
        #c5d4ff 60%,
        #e0e8ff 85%,
        rgba(250, 250, 250, 0) 100%
      );
  }
  .chip {
    backdrop-filter: blur(8px);
  }
  .full-width-header {
    margin-left: calc(-50vw + 50%);
    margin-right: calc(-50vw + 50%);
    margin-top: -1.5rem;
    width: 100vw;
    position: relative;
  }
</style>
<header class="sky full-width-header">
  <div class="fixed right-2 top-2 sm:right-6 sm:top-6 z-50">
    <button id="themeBtn" class="chip inline-flex items-center gap-2 rounded-full border border-white/40 bg-white/70 px-3 py-1 text-xs font-medium text-neutral-700 shadow-sm transition hover:bg-white/70">
      <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 756 756" fill="none">
        <g clip-path="url(#clip0_392_73)">
          <path d="M590.344 61.7195H540.967C527.611 61.7195 515.065 68.5998 507.375 79.9321L106.697 687.425C103.459 692.686 107.102 699.567 113.173 699.567H162.549C175.905 699.567 188.451 692.686 196.141 681.354L596.819 73.8612C600.462 69.0045 596.415 61.7195 590.344 61.7195Z" fill="#FFC000"/>
          <path fill-rule="evenodd" clip-rule="evenodd" d="M174.894 36L191.087 91.1066C205.431 141.076 244.758 180.305 294.728 194.782L349.787 210.66L294.728 226.538C244.758 241.015 205.431 280.244 191.087 330.214L174.894 385.787L158.7 330.681C144.357 280.711 105.029 241.482 55.0591 227.005L0 211.127L55.0591 195.249C105.029 180.772 144.357 141.543 158.7 91.5736L174.894 36Z" fill="#FFC000"/>
          <path d="M579.162 475.149C583.628 492.209 630.825 537.178 646.514 542.914C630.825 546.853 584.383 593.294 579.162 610.679C574.695 593.619 530.202 546.784 511.809 542.914C530.202 535.243 574.226 492.209 579.162 475.149ZM578.692 365.212L562.26 421.603C547.706 472.307 507.8 512.112 457.095 526.802L401.227 542.914L457.095 559.026C507.8 573.716 547.706 613.521 562.26 664.226L578.692 720.143L595.124 663.752C609.678 613.047 649.584 573.242 700.289 558.552L756.158 542.44L700.289 526.329C649.584 511.639 609.678 471.833 595.124 421.129L578.692 365.212Z" fill="#FFC000"/>
        </g>
        <defs>
          <clipPath id="clip0_392_73">
            <rect width="756" height="756" fill="white"/>
          </clipPath>
        </defs>
      </svg>
      Powered by Cycls
    </button>
  </div>
  <svg class="pointer-events-none absolute -top-10 right-0 h-64 w-auto opacity-20" viewBox="0 0 500 200" aria-hidden="true">
    <path d="M0,120 C120,80 220,60 360,40 C430,30 480,40 500,60 L500,0 L0,0 Z" fill="white"/>
  </svg>
  <div class="mx-auto max-w-6xl px-4 pt-20 pb-16 sm:pt-24 sm:pb-20">
    <h1 class="text-center text-3xl font-extrabold tracking-tight sm:text-5xl">
      Intelligence meets <span class="bg-gradient-to-r from-neutral-900 to-neutral-600 bg-clip-text text-transparent">Investing</span>
    </h1>
    <p class="mx-auto mt-3 max-w-3xl text-center text-sm text-neutral-700 sm:text-base">
      Ask questions in any language. Get instant market insights, real‑time data, and AI‑powered analysis that helps you make smarter investment decisions.
    </p>
    <div class="mt-6 flex flex-wrap items-center justify-center gap-2 text-[11px] sm:text-xs">
      <span class="chip rounded-full border border-white/60 bg-white/70 px-3 py-1 text-neutral-700 shadow-sm">Real‑time prices</span>
      <span class="chip rounded-full border border-white/60 bg-white/70 px-3 py-1 text-neutral-700 shadow-sm">Live market data</span>
      <span class="chip rounded-full border border-white/60 bg-white/70 px-3 py-1 text-neutral-700 shadow-sm">AI‑powered</span>
      <a href="https://github.com/Cycls/Stocks-Agent" class="inline-flex items-center gap-2 rounded-lg bg-black px-4 py-1.5 text-xs font-semibold text-white shadow-sm transition hover:bg-neutral-800">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="h-4 w-4" fill="currentColor">
          <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/>
        </svg>
        GitHub
      </a>
    </div>
    </div>
  </div>
</header>
</raw>
"""

intro = f"""
<div class="mx-auto mt-20 max-w-4xl">
  <div class="flex flex-wrap items-center justify-center gap-3">
    <a href="https://cycls.com/send/{urllib.parse.quote('Compare AAPL vs MSFT YTD')}" class="prompt chip group rounded-2xl border border-neutral-200 bg-white px-4 py-2 text-sm shadow-sm transition hover:shadow-md">
      Compare <span class="font-semibold">AAPL</span> vs <span class="font-semibold">MSFT</span> YTD
    </a>
    <a href="https://cycls.com/send/{urllib.parse.quote("What's the current price of NVDA?")}" class="prompt chip rounded-2xl border border-neutral-200 bg-white px-4 py-2 text-sm shadow-sm transition hover:shadow-md">
      What's the current price of <span class="font-semibold">NVDA</span>?
    </a>
    <a href="https://cycls.com/send/{urllib.parse.quote('Show top gainers today')}" class="prompt chip rounded-2xl border border-neutral-200 bg-white px-4 py-2 text-sm shadow-sm transition hover:shadow-md">
      Show <span class="font-semibold">top gainers</span> today
    </a>
    <a href="https://cycls.com/send/{urllib.parse.quote('Simple analysis on TSLA')}" class="prompt chip rounded-2xl border border-neutral-200 bg-white px-4 py-2 text-sm shadow-sm transition hover:shadow-md">
      Simple analysis on <span class="font-semibold">TSLA</span>
    </a>
  </div>
</div>
"""