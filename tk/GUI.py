





<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://github.githubassets.com">
  <link rel="dns-prefetch" href="https://avatars0.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars1.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars2.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars3.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">



  <link crossorigin="anonymous" media="all" integrity="sha512-8B5lvNq1b88YJg2eQ7wXcWwl490xeelSavDDj7NEOtpEK7m0tKkmFi9BDX+S+nYyh/teAumil+CjK/AscuQrdg==" rel="stylesheet" href="https://github.githubassets.com/assets/frameworks-081940cf9af751b35bb9fd062060601a.css" />
  <link crossorigin="anonymous" media="all" integrity="sha512-vozupRTrzo7k2NwiAgC37o0fUpxqBtSeDrVyaxH6I+ed18h/6awTfjJ5uRMyNRb/2rOxZtsTi8FKLv7DVZMZwg==" rel="stylesheet" href="https://github.githubassets.com/assets/site-c24aa206cdd4fb0b962ca6e303f5faca.css" />
    <link crossorigin="anonymous" media="all" integrity="sha512-KOqqPXmPgXnSCDE/RVobSMDp3N81KrS5yqxFG9e6gN2YdLVtBZtRXT/0f3YHTGU2PwyqLmcBdz6bARkVDb4Nhg==" rel="stylesheet" href="https://github.githubassets.com/assets/github-f596d1693f63c9206f4e5d91b1c00078.css" />
    
    
    
    

  <meta name="viewport" content="width=device-width">
  
  <title>BISIP/GUI.py at master · clberube/BISIP · GitHub</title>
    <meta name="description" content="BISIP - Bayesian inference of spectral induced polarization parameters - clberube/BISIP">
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
  <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
  <meta property="fb:app_id" content="1401488693436528">

    <meta name="twitter:image:src" content="https://avatars0.githubusercontent.com/u/20193582?s=400&amp;v=4" /><meta name="twitter:site" content="@github" /><meta name="twitter:card" content="summary" /><meta name="twitter:title" content="clberube/BISIP" /><meta name="twitter:description" content="BISIP - Bayesian inference of spectral induced polarization parameters - clberube/BISIP" />
    <meta property="og:image" content="https://avatars0.githubusercontent.com/u/20193582?s=400&amp;v=4" /><meta property="og:site_name" content="GitHub" /><meta property="og:type" content="object" /><meta property="og:title" content="clberube/BISIP" /><meta property="og:url" content="https://github.com/clberube/BISIP" /><meta property="og:description" content="BISIP - Bayesian inference of spectral induced polarization parameters - clberube/BISIP" />

  <link rel="assets" href="https://github.githubassets.com/">
  
  <meta name="pjax-timeout" content="1000">
  
  <meta name="request-id" content="A948:0EFC:6E311:B344F:5D3E36C5" data-pjax-transient>


  

  <meta name="selected-link" value="repo_source" data-pjax-transient>

      <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
    <meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
    <meta name="google-site-verification" content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc">

  <meta name="octolytics-host" content="collector.githubapp.com" /><meta name="octolytics-app-id" content="github" /><meta name="octolytics-event-url" content="https://collector.githubapp.com/github-external/browser_event" /><meta name="octolytics-dimension-request_id" content="A948:0EFC:6E311:B344F:5D3E36C5" /><meta name="octolytics-dimension-region_edge" content="iad" /><meta name="octolytics-dimension-region_render" content="iad" />
<meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" />



    <meta name="google-analytics" content="UA-3769691-2">


<meta class="js-ga-set" name="dimension1" content="Logged Out">



  

      <meta name="hostname" content="github.com">
    <meta name="user-login" content="">

      <meta name="expected-hostname" content="github.com">
    <meta name="js-proxy-site-detection-payload" content="MTdkYTlkYzU1MDMwMDVjMDYwNTUyZTYwODA2NjE4ZmJmN2E2NWQ4NTljNWMwOTlmMmI4M2EyNTZjZTBmMjRmM3x7InJlbW90ZV9hZGRyZXNzIjoiMTg2LjIwNy4xODIuMTkzIiwicmVxdWVzdF9pZCI6IkE5NDg6MEVGQzo2RTMxMTpCMzQ0Rjo1RDNFMzZDNSIsInRpbWVzdGFtcCI6MTU2NDM1ODM1MiwiaG9zdCI6ImdpdGh1Yi5jb20ifQ==">

    <meta name="enabled-features" content="MARKETPLACE_FEATURED_BLOG_POSTS,MARKETPLACE_INVOICED_BILLING,MARKETPLACE_SOCIAL_PROOF_CUSTOMERS,MARKETPLACE_TRENDING_SOCIAL_PROOF,MARKETPLACE_RECOMMENDATIONS,MARKETPLACE_PENDING_INSTALLATIONS">

  <meta name="html-safe-nonce" content="546c622d31a9a2ec5e66b1712cd3ec8bb5bd52dc">

  <meta http-equiv="x-pjax-version" content="3c1643205f794dc4e59e8a316923fc4f">
  

      <link href="https://github.com/clberube/BISIP/commits/master.atom" rel="alternate" title="Recent Commits to BISIP:master" type="application/atom+xml">

  <meta name="go-import" content="github.com/clberube/BISIP git https://github.com/clberube/BISIP.git">

  <meta name="octolytics-dimension-user_id" content="20193582" /><meta name="octolytics-dimension-user_login" content="clberube" /><meta name="octolytics-dimension-repository_id" content="62168095" /><meta name="octolytics-dimension-repository_nwo" content="clberube/BISIP" /><meta name="octolytics-dimension-repository_public" content="true" /><meta name="octolytics-dimension-repository_is_fork" content="false" /><meta name="octolytics-dimension-repository_network_root_id" content="62168095" /><meta name="octolytics-dimension-repository_network_root_nwo" content="clberube/BISIP" /><meta name="octolytics-dimension-repository_explore_github_marketplace_ci_cta_shown" content="false" />


    <link rel="canonical" href="https://github.com/clberube/BISIP/blob/master/bisip/GUI.py" data-pjax-transient>


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <link rel="mask-icon" href="https://github.githubassets.com/pinned-octocat.svg" color="#000000">
  <link rel="icon" type="image/x-icon" class="js-site-favicon" href="https://github.githubassets.com/favicon.ico">

<meta name="theme-color" content="#1e2327">





  <link rel="manifest" href="/manifest.json" crossOrigin="use-credentials">

  </head>

  <body class="logged-out env-production page-responsive page-blob">
    

  <div class="position-relative js-header-wrapper ">
    <a href="#start-of-content" tabindex="1" class="px-2 py-4 bg-blue text-white show-on-focus js-skip-to-content">Skip to content</a>
    <div id="js-pjax-loader-bar" class="pjax-loader-bar"><div class="progress"></div></div>

    
    
    


        <header class="Header-old header-logged-out js-details-container Details position-relative f4 py-2" role="banner">
  <div class="container-lg d-lg-flex flex-items-center p-responsive">
    <div class="d-flex flex-justify-between flex-items-center">
        <a class="mr-4" href="https://github.com/" aria-label="Homepage" data-ga-click="(Logged out) Header, go to homepage, icon:logo-wordmark">
          <svg height="32" class="octicon octicon-mark-github text-white" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
        </a>

          <div class="d-lg-none css-truncate css-truncate-target width-fit p-2">
            
              <svg class="octicon octicon-repo" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
    <a class="Header-link" href="/clberube">clberube</a>
    /
    <a class="Header-link" href="/clberube/BISIP">BISIP</a>


          </div>

        <div class="d-flex flex-items-center">
            <a href="/join?source=header-repo"
              class="d-inline-block d-lg-none f5 text-white no-underline border border-gray-dark rounded-2 px-2 py-1 mr-3 mr-sm-5"
              data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;client_id&quot;:&quot;2144787863.1564358206&quot;,&quot;originating_request_id&quot;:&quot;A948:0EFC:6E311:B344F:5D3E36C5&quot;,&quot;originating_url&quot;:&quot;https://github.com/clberube/BISIP/blob/master/bisip/GUI.py&quot;,&quot;referrer&quot;:&quot;https://github.com/clberube/BISIP/tree/master/bisip&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="f2604e653c80088fbbc47eec38ebcc228c7c8605220483046561d62c9a5bb466"
              data-ga-click="(Logged out) Header, clicked Sign up, text:sign-up">
              Sign&nbsp;up
            </a>

          <button class="btn-link d-lg-none mt-1 js-details-target" type="button" aria-label="Toggle navigation" aria-expanded="false">
            <svg height="24" class="octicon octicon-three-bars text-white" viewBox="0 0 12 16" version="1.1" width="18" aria-hidden="true"><path fill-rule="evenodd" d="M11.41 9H.59C0 9 0 8.59 0 8c0-.59 0-1 .59-1H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1h.01zm0-4H.59C0 5 0 4.59 0 4c0-.59 0-1 .59-1H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1h.01zM.59 11H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1H.59C0 13 0 12.59 0 12c0-.59 0-1 .59-1z"/></svg>
          </button>
        </div>
    </div>

    <div class="HeaderMenu HeaderMenu--logged-out position-fixed top-0 right-0 bottom-0 height-fit position-lg-relative d-lg-flex flex-justify-between flex-items-center flex-auto">
      <div class="d-flex d-lg-none flex-justify-end border-bottom bg-gray-light p-3">
        <button class="btn-link js-details-target" type="button" aria-label="Toggle navigation" aria-expanded="false">
          <svg height="24" class="octicon octicon-x text-gray" viewBox="0 0 12 16" version="1.1" width="18" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
        </button>
      </div>

        <nav class="mt-0 px-3 px-lg-0 mb-5 mb-lg-0" aria-label="Global">
          <ul class="d-lg-flex list-style-none">
              <li class="d-block d-lg-flex flex-lg-nowrap flex-lg-items-center border-bottom border-lg-bottom-0 mr-0 mr-lg-3 edge-item-fix position-relative flex-wrap flex-justify-between d-flex flex-items-center ">
                <details class="HeaderMenu-details details-overlay details-reset width-full">
                  <summary class="HeaderMenu-summary HeaderMenu-link px-0 py-3 border-0 no-wrap d-block d-lg-inline-block">
                    Why GitHub?
                    <svg x="0px" y="0px" viewBox="0 0 14 8" xml:space="preserve" fill="none" class="icon-chevon-down-mktg position-absolute position-lg-relative">
                      <path d="M1,1l6.2,6L13,1"></path>
                    </svg>
                  </summary>
                  <div class="dropdown-menu flex-auto rounded-1 bg-white px-0 mt-0 pb-4 p-lg-4 position-relative position-lg-absolute left-0 left-lg-n4">
                    <a href="/features" class="py-2 lh-condensed-ultra d-block link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Features">Features <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a>
                    <ul class="list-style-none f5 pb-3">
                      <li class="edge-item-fix"><a href="/features/code-review/" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Code review">Code review</a></li>
                      <li class="edge-item-fix"><a href="/features/project-management/" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Project management">Project management</a></li>
                      <li class="edge-item-fix"><a href="/features/integrations" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Integrations">Integrations</a></li>
                      <li class="edge-item-fix"><a href="/features/actions" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Actions">Actions</a>
                          <li class="edge-item-fix"><a href="/features/package-registry" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Package Registry">Package registry</a>
                      <li class="edge-item-fix"><a href="/features#team-management" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Team management">Team management</a></li>
                      <li class="edge-item-fix"><a href="/features#social-coding" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Social coding">Social coding</a></li>
                      <li class="edge-item-fix"><a href="/features#documentation" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Documentation">Documentation</a></li>
                      <li class="edge-item-fix"><a href="/features#code-hosting" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Code hosting">Code hosting</a></li>
                    </ul>

                    <ul class="list-style-none mb-0 border-lg-top pt-lg-3">
                      <li class="edge-item-fix"><a href="/customer-stories" class="py-2 lh-condensed-ultra d-block no-underline link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Customer stories">Customer stories <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a></li>
                      <li class="edge-item-fix"><a href="/security" class="py-2 lh-condensed-ultra d-block no-underline link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Security">Security <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a></li>
                    </ul>
                  </div>
                </details>
              </li>
              <li class="border-bottom border-lg-bottom-0 mr-0 mr-lg-3">
                <a href="/enterprise" class="HeaderMenu-link no-underline py-3 d-block d-lg-inline-block" data-ga-click="(Logged out) Header, go to Enterprise">Enterprise</a>
              </li>

              <li class="d-block d-lg-flex flex-lg-nowrap flex-lg-items-center border-bottom border-lg-bottom-0 mr-0 mr-lg-3 edge-item-fix position-relative flex-wrap flex-justify-between d-flex flex-items-center ">
                <details class="HeaderMenu-details details-overlay details-reset width-full">
                  <summary class="HeaderMenu-summary HeaderMenu-link px-0 py-3 border-0 no-wrap d-block d-lg-inline-block">
                    Explore
                    <svg x="0px" y="0px" viewBox="0 0 14 8" xml:space="preserve" fill="none" class="icon-chevon-down-mktg position-absolute position-lg-relative">
                      <path d="M1,1l6.2,6L13,1"></path>
                    </svg>
                  </summary>

                  <div class="dropdown-menu flex-auto rounded-1 bg-white px-0 pt-2 pb-0 mt-0 pb-4 p-lg-4 position-relative position-lg-absolute left-0 left-lg-n4">
                    <ul class="list-style-none mb-3">
                      <li class="edge-item-fix"><a href="/explore" class="py-2 lh-condensed-ultra d-block link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Explore">Explore GitHub <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a></li>
                    </ul>

                    <h4 class="text-gray-light text-normal text-mono f5 mb-2 border-lg-top pt-lg-3">Learn &amp; contribute</h4>
                    <ul class="list-style-none mb-3">
                      <li class="edge-item-fix"><a href="/topics" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Topics">Topics</a></li>
                        <li class="edge-item-fix"><a href="/collections" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Collections">Collections</a></li>
                      <li class="edge-item-fix"><a href="/trending" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Trending">Trending</a></li>
                      <li class="edge-item-fix"><a href="https://lab.github.com/" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Learning lab">Learning Lab</a></li>
                      <li class="edge-item-fix"><a href="https://opensource.guide" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Open source guides">Open source guides</a></li>
                    </ul>

                    <h4 class="text-gray-light text-normal text-mono f5 mb-2 border-lg-top pt-lg-3">Connect with others</h4>
                    <ul class="list-style-none mb-0">
                      <li class="edge-item-fix"><a href="https://github.com/events" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Events">Events</a></li>
                      <li class="edge-item-fix"><a href="https://github.community" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Community forum">Community forum</a></li>
                      <li class="edge-item-fix"><a href="https://education.github.com" class="py-2 pb-0 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to GitHub Education">GitHub Education</a></li>
                    </ul>
                  </div>
                </details>
              </li>

              <li class="border-bottom border-lg-bottom-0 mr-0 mr-lg-3">
                <a href="/marketplace" class="HeaderMenu-link no-underline py-3 d-block d-lg-inline-block" data-ga-click="(Logged out) Header, go to Marketplace">Marketplace</a>
              </li>

              <li class="d-block d-lg-flex flex-lg-nowrap flex-lg-items-center border-bottom border-lg-bottom-0 mr-0 mr-lg-3 edge-item-fix position-relative flex-wrap flex-justify-between d-flex flex-items-center ">
                <details class="HeaderMenu-details details-overlay details-reset width-full">
                  <summary class="HeaderMenu-summary HeaderMenu-link px-0 py-3 border-0 no-wrap d-block d-lg-inline-block">
                    Pricing
                    <svg x="0px" y="0px" viewBox="0 0 14 8" xml:space="preserve" fill="none" class="icon-chevon-down-mktg position-absolute position-lg-relative">
                       <path d="M1,1l6.2,6L13,1"></path>
                    </svg>
                  </summary>

                  <div class="dropdown-menu flex-auto rounded-1 bg-white px-0 pt-2 pb-4 mt-0 p-lg-4 position-relative position-lg-absolute left-0 left-lg-n4">
                    <a href="/pricing" class="pb-2 lh-condensed-ultra d-block link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Pricing">Plans <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a>

                    <ul class="list-style-none mb-3">
                      <li class="edge-item-fix"><a href="/pricing#feature-comparison" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Compare plans">Compare plans</a></li>
                      <li class="edge-item-fix"><a href="https://enterprise.github.com/contact" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Contact Sales">Contact Sales</a></li>
                    </ul>

                    <ul class="list-style-none mb-0 border-lg-top pt-lg-3">
                      <li class="edge-item-fix"><a href="/nonprofit" class="py-2 lh-condensed-ultra d-block no-underline link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Nonprofits">Nonprofit <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a></li>
                      <li class="edge-item-fix"><a href="https://education.github.com" class="py-2 pb-0 lh-condensed-ultra d-block no-underline link-gray-dark no-underline h5 Bump-link--hover"  data-ga-click="(Logged out) Header, go to Education">Education <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a></li>
                    </ul>
                  </div>
                </details>
              </li>
          </ul>
        </nav>

      <div class="d-lg-flex flex-items-center px-3 px-lg-0 text-center text-lg-left">
          <div class="d-lg-flex mb-3 mb-lg-0">
            <div class="header-search flex-self-stretch flex-lg-self-auto mr-0 mr-lg-3 mb-3 mb-lg-0 scoped-search site-scoped-search js-site-search position-relative js-jump-to"
  role="combobox"
  aria-owns="jump-to-results"
  aria-label="Search or jump to"
  aria-haspopup="listbox"
  aria-expanded="false"
>
  <div class="position-relative">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-site-search-form" role="search" aria-label="Site" data-scope-type="Repository" data-scope-id="62168095" data-scoped-search-url="/clberube/BISIP/search" data-unscoped-search-url="/search" action="/clberube/BISIP/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
      <label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container">
        <input type="text"
          class="form-control input-sm header-search-input jump-to-field js-jump-to-field js-site-search-focus js-site-search-field is-clearable"
          data-hotkey="s,/"
          name="q"
          value=""
          placeholder="Search"
          data-unscoped-placeholder="Search GitHub"
          data-scoped-placeholder="Search"
          autocapitalize="off"
          aria-autocomplete="list"
          aria-controls="jump-to-results"
          aria-label="Search"
          data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations#csrf-token=ywjZh2FT2LKLRP34Xzvs+E2XH6/IxCHaKSxHXnKlQg9r8r4jXGJIlpxe/blrqCm7RoK7iaSmO2XPTwOn4EOOBQ=="
          spellcheck="false"
          autocomplete="off"
          >
          <input type="hidden" class="js-site-search-type-field" name="type" >
            <img src="https://github.githubassets.com/images/search-key-slash.svg" alt="" class="mr-2 header-search-key-slash">

            <div class="Box position-absolute overflow-hidden d-none jump-to-suggestions js-jump-to-suggestions-container">
              
<ul class="d-none js-jump-to-suggestions-template-container">
  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-suggestion" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0 0 13 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 0 0 0-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"/></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

</ul>

<ul class="d-none js-jump-to-no-results-template-container">
  <li class="d-flex flex-justify-center flex-items-center f5 d-none js-jump-to-suggestion p-2">
    <span class="text-gray">No suggested jump to results</span>
  </li>
</ul>

<ul id="jump-to-results" role="listbox" class="p-0 m-0 js-navigation-container jump-to-suggestions-results-container js-jump-to-suggestions-results-container">
  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-scoped-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0 0 13 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 0 0 0-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"/></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-global-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0 0 13 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 0 0 0-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"/></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>


</ul>

            </div>
      </label>
</form>  </div>
</div>

          </div>

        <a href="/login?return_to=%2Fclberube%2FBISIP%2Fblob%2Fmaster%2Fbisip%2FGUI.py"
          class="HeaderMenu-link no-underline mr-3"
          data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header menu&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;client_id&quot;:&quot;2144787863.1564358206&quot;,&quot;originating_request_id&quot;:&quot;A948:0EFC:6E311:B344F:5D3E36C5&quot;,&quot;originating_url&quot;:&quot;https://github.com/clberube/BISIP/blob/master/bisip/GUI.py&quot;,&quot;referrer&quot;:&quot;https://github.com/clberube/BISIP/tree/master/bisip&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="ec7031876f357406fc809a7a4bf454ca6212f591fe91485166bf73cd485da4dd"
          data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in">
          Sign&nbsp;in
        </a>
          <a href="/join?source=header-repo"
            class="HeaderMenu-link d-inline-block no-underline border border-gray-dark rounded-1 px-2 py-1"
            data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header menu&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;client_id&quot;:&quot;2144787863.1564358206&quot;,&quot;originating_request_id&quot;:&quot;A948:0EFC:6E311:B344F:5D3E36C5&quot;,&quot;originating_url&quot;:&quot;https://github.com/clberube/BISIP/blob/master/bisip/GUI.py&quot;,&quot;referrer&quot;:&quot;https://github.com/clberube/BISIP/tree/master/bisip&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="ec7031876f357406fc809a7a4bf454ca6212f591fe91485166bf73cd485da4dd"
            data-ga-click="(Logged out) Header, clicked Sign up, text:sign-up">
            Sign&nbsp;up
          </a>
      </div>
    </div>
  </div>
</header>

  </div>

  <div id="start-of-content" class="show-on-focus"></div>


    <div id="js-flash-container">

</div>



  <div class="application-main " data-commit-hovercards-enabled>
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode" class="">
    <main  >
      


  








  <div class="pagehead repohead instapaper_ignore readability-menu experiment-repo-nav pt-0 pt-lg-4 ">
    <div class="repohead-details-container clearfix container-lg p-responsive d-none d-lg-block">

      <ul class="pagehead-actions">




  <li>
    
  <a class="tooltipped tooltipped-s btn btn-sm btn-with-count" aria-label="You must be signed in to watch a repository" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;notification subscription menu watch&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;client_id&quot;:&quot;2144787863.1564358206&quot;,&quot;originating_request_id&quot;:&quot;A948:0EFC:6E311:B344F:5D3E36C5&quot;,&quot;originating_url&quot;:&quot;https://github.com/clberube/BISIP/blob/master/bisip/GUI.py&quot;,&quot;referrer&quot;:&quot;https://github.com/clberube/BISIP/tree/master/bisip&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="2d1033e5cecf10f11ca820a459a14f57ff1190f5f15877e8872cbfc135051ae6" href="/login?return_to=%2Fclberube%2FBISIP">
    <svg class="octicon octicon-eye v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
    Watch
</a>    <a class="social-count" href="/clberube/BISIP/watchers"
       aria-label="3 users are watching this repository">
      3
    </a>

  </li>

  <li>
        <a class="btn btn-sm btn-with-count tooltipped tooltipped-s" aria-label="You must be signed in to star a repository" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;star button&quot;,&quot;repository_id&quot;:62168095,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;client_id&quot;:&quot;2144787863.1564358206&quot;,&quot;originating_request_id&quot;:&quot;A948:0EFC:6E311:B344F:5D3E36C5&quot;,&quot;originating_url&quot;:&quot;https://github.com/clberube/BISIP/blob/master/bisip/GUI.py&quot;,&quot;referrer&quot;:&quot;https://github.com/clberube/BISIP/tree/master/bisip&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="7d6898c41b42efc92edaf2082dfa57adcddd49aef79bd0acd7c353d835abd377" href="/login?return_to=%2Fclberube%2FBISIP">
      <svg class="octicon octicon-star v-align-text-bottom" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74L14 6z"/></svg>
      Star
</a>
    <a class="social-count js-social-count" href="/clberube/BISIP/stargazers"
      aria-label="6 users starred this repository">
      6
    </a>

  </li>

  <li>
      <a class="btn btn-sm btn-with-count tooltipped tooltipped-s" aria-label="You must be signed in to fork a repository" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;repo details fork button&quot;,&quot;repository_id&quot;:62168095,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;client_id&quot;:&quot;2144787863.1564358206&quot;,&quot;originating_request_id&quot;:&quot;A948:0EFC:6E311:B344F:5D3E36C5&quot;,&quot;originating_url&quot;:&quot;https://github.com/clberube/BISIP/blob/master/bisip/GUI.py&quot;,&quot;referrer&quot;:&quot;https://github.com/clberube/BISIP/tree/master/bisip&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="f175eaaafba7442df5f0eb2aaf13b7a732c97f2e1e31709ddd4df6469a246176" href="/login?return_to=%2Fclberube%2FBISIP">
        <svg class="octicon octicon-repo-forked v-align-text-bottom" viewBox="0 0 10 16" version="1.1" width="10" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
        Fork
</a>
    <a href="/clberube/BISIP/network/members" class="social-count"
       aria-label="2 users forked this repository">
      2
    </a>
  </li>
</ul>

      <h1 class="public ">
    <svg class="octicon octicon-repo" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
  <span class="author" itemprop="author"><a class="url fn" rel="author" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=20193582" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/clberube">clberube</a></span><!--
--><span class="path-divider">/</span><!--
--><strong itemprop="name"><a data-pjax="#js-repo-pjax-container" href="/clberube/BISIP">BISIP</a></strong>
  

</h1>

    </div>
    
<nav class="hx_reponav reponav js-repo-nav js-sidenav-container-pjax container-lg p-responsive d-none d-lg-block"
     itemscope
     itemtype="http://schema.org/BreadcrumbList"
    aria-label="Repository"
     data-pjax="#js-repo-pjax-container">

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a class="js-selected-navigation-item selected reponav-item" itemprop="url" data-hotkey="g c" aria-current="page" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages /clberube/BISIP" href="/clberube/BISIP">
      <svg class="octicon octicon-code" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"/></svg>
      <span itemprop="name">Code</span>
      <meta itemprop="position" content="1">
</a>  </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a itemprop="url" data-hotkey="g i" class="js-selected-navigation-item reponav-item" data-selected-links="repo_issues repo_labels repo_milestones /clberube/BISIP/issues" href="/clberube/BISIP/issues">
        <svg class="octicon octicon-issue-opened" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"/></svg>
        <span itemprop="name">Issues</span>
        <span class="Counter">1</span>
        <meta itemprop="position" content="2">
</a>    </span>

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a data-hotkey="g p" itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_pulls checks /clberube/BISIP/pulls" href="/clberube/BISIP/pulls">
      <svg class="octicon octicon-git-pull-request" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
      <span itemprop="name">Pull requests</span>
      <span class="Counter">0</span>
      <meta itemprop="position" content="3">
</a>  </span>


    <a data-hotkey="g b" class="js-selected-navigation-item reponav-item" data-selected-links="repo_projects new_repo_project repo_project /clberube/BISIP/projects" href="/clberube/BISIP/projects">
      <svg class="octicon octicon-project" viewBox="0 0 15 16" version="1.1" width="15" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      Projects
      <span class="Counter" >0</span>
</a>


    <a data-skip-pjax="true" class="js-selected-navigation-item reponav-item" data-selected-links="security alerts policy /clberube/BISIP/security/advisories" href="/clberube/BISIP/security/advisories">
      <svg class="octicon octicon-shield" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M0 2l7-2 7 2v6.02C14 12.69 8.69 16 7 16c-1.69 0-7-3.31-7-7.98V2zm1 .75L7 1l6 1.75v5.268C13 12.104 8.449 15 7 15c-1.449 0-6-2.896-6-6.982V2.75zm1 .75L7 2v12c-1.207 0-5-2.482-5-5.985V3.5z"/></svg>
      Security
</a>
    <a class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors dependency_graph pulse people /clberube/BISIP/pulse" href="/clberube/BISIP/pulse">
      <svg class="octicon octicon-graph" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z"/></svg>
      Insights
</a>

</nav>

  <div class="reponav-wrapper reponav-small d-lg-none">
  <nav class="reponav js-reponav text-center no-wrap"
       itemscope
       itemtype="http://schema.org/BreadcrumbList">

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a class="js-selected-navigation-item selected reponav-item" itemprop="url" aria-current="page" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages /clberube/BISIP" href="/clberube/BISIP">
        <span itemprop="name">Code</span>
        <meta itemprop="position" content="1">
</a>    </span>

      <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
        <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_issues repo_labels repo_milestones /clberube/BISIP/issues" href="/clberube/BISIP/issues">
          <span itemprop="name">Issues</span>
          <span class="Counter">1</span>
          <meta itemprop="position" content="2">
</a>      </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_pulls checks /clberube/BISIP/pulls" href="/clberube/BISIP/pulls">
        <span itemprop="name">Pull requests</span>
        <span class="Counter">0</span>
        <meta itemprop="position" content="3">
</a>    </span>

      <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
        <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_projects new_repo_project repo_project /clberube/BISIP/projects" href="/clberube/BISIP/projects">
          <span itemprop="name">Projects</span>
          <span class="Counter">0</span>
          <meta itemprop="position" content="4">
</a>      </span>


      <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="security alerts policy /clberube/BISIP/security/advisories" href="/clberube/BISIP/security/advisories">
        <span itemprop="name">Security</span>
        <meta itemprop="position" content="6">
</a>
      <a class="js-selected-navigation-item reponav-item" data-selected-links="pulse /clberube/BISIP/pulse" href="/clberube/BISIP/pulse">
        Pulse
</a>

  </nav>
</div>


  </div>
<div class="container-lg clearfix new-discussion-timeline experiment-repo-nav  p-responsive">
  <div class="repository-content ">

    
    


  
    <a class="d-none js-permalink-shortcut" data-hotkey="y" href="/clberube/BISIP/blob/5b08fc447e6ac66fc9a50c441b9cc2155725d018/bisip/GUI.py">Permalink</a>

    <!-- blob contrib key: blob_contributors:v21:d20315415546da8ae9f76a07d092714f -->
          <div class="signup-prompt mx-auto mb-6 p-4 border rounded-2"
      style="background-image: url('https://github.githubassets.com/images/modules/site/heroes/octocat-unpacking-hubot.svg'); background-position: 94% 96%; background-size: auto 170%;">
      <div class="position-relative">
        <!-- '"` --><!-- </textarea></xmp> --></option></form><form action="/prompt_dismissals/blobs" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="_method" value="put" /><input type="hidden" name="authenticity_token" value="yUGlVKAIyGC/xj1JomiFRVNTAvMhtMqzm+WhdmpbdyC0ka6PIYajy9MOYz6O8D0TrJ0SD0cB6lXmBTivUJ8efw==" />
          <button
            type="submit"
            class="position-absolute top-0 right-0 py-1 px-2 border bg-white btn-link link-gray no-underline f6"
            data-ga-click="(Logged out) Sign up prompt, click, text:Dismiss"
            data-ga-load="Blob, view, type:redesigned signup prompt">
            Dismiss
          </button>
</form>        <h3>All your code in one place</h3>
        <p class="col-md-7">
          GitHub makes it easy to scale back on context switching. Read rendered
          documentation, see the history of any file, and collaborate with
          contributors on projects across GitHub.
        </p>
        <a href="/join?source=prompt-blob-show"
          class="btn btn-primary mr-2"
          data-ga-click="(Logged out) Sign up prompt, click, text:Sign up for free"
          data-ga-load="Blob, view, type:redesigned signup prompt">
          Sign up for free
        </a>
        <a href="/pricing"
          data-ga-click="(Logged out) Sign up prompt, click, text:See pricing for teams and enterprises"
          data-ga-load="Blob, view, type:redesigned signup prompt">
          See pricing for teams and enterprises
        </a>
      </div>
    </div>


    <div class="d-flex flex-items-start flex-shrink-0 mb-2 flex-column flex-md-row">
      <span class="d-flex flex-justify-between width-full width-md-auto">
        
<details class="details-reset details-overlay select-menu branch-select-menu  hx_rsm" id="branch-select-menu">
  <summary class="btn btn-sm select-menu-button css-truncate"
           data-hotkey="w"
           
           title="Switch branches or tags">
    <i>Branch:</i>
    <span class="css-truncate-target">master</span>
  </summary>

  <details-menu class="select-menu-modal hx_rsm-modal position-absolute" style="z-index: 99;" src="/clberube/BISIP/ref-list/master/bisip/GUI.py?source_action=show&amp;source_controller=blob" preload>
    <include-fragment class="select-menu-loading-overlay anim-pulse">
      <svg height="32" class="octicon octicon-octoface" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M14.7 5.34c.13-.32.55-1.59-.13-3.31 0 0-1.05-.33-3.44 1.3-1-.28-2.07-.32-3.13-.32s-2.13.04-3.13.32c-2.39-1.64-3.44-1.3-3.44-1.3-.68 1.72-.26 2.99-.13 3.31C.49 6.21 0 7.33 0 8.69 0 13.84 3.33 15 7.98 15S16 13.84 16 8.69c0-1.36-.49-2.48-1.3-3.35zM8 14.02c-3.3 0-5.98-.15-5.98-3.35 0-.76.38-1.48 1.02-2.07 1.07-.98 2.9-.46 4.96-.46 2.07 0 3.88-.52 4.96.46.65.59 1.02 1.3 1.02 2.07 0 3.19-2.68 3.35-5.98 3.35zM5.49 9.01c-.66 0-1.2.8-1.2 1.78s.54 1.79 1.2 1.79c.66 0 1.2-.8 1.2-1.79s-.54-1.78-1.2-1.78zm5.02 0c-.66 0-1.2.79-1.2 1.78s.54 1.79 1.2 1.79c.66 0 1.2-.8 1.2-1.79s-.53-1.78-1.2-1.78z"/></svg>
    </include-fragment>
  </details-menu>
</details>

        <div class="BtnGroup flex-shrink-0 d-md-none">
          <a href="/clberube/BISIP/find/master"
                class="js-pjax-capture-input btn btn-sm BtnGroup-item"
                data-pjax
                data-hotkey="t">
            Find file
          </a>
          <clipboard-copy value="bisip/GUI.py" class="btn btn-sm BtnGroup-item">
            Copy path
          </clipboard-copy>
        </div>
      </span>
      <h2 id="blob-path" class="breadcrumb flex-auto min-width-0 text-normal flex-md-self-center ml-md-2 mr-md-3 my-2 my-md-0">
        <span class="js-repo-root text-bold"><span class="js-path-segment"><a data-pjax="true" href="/clberube/BISIP"><span>BISIP</span></a></span></span><span class="separator">/</span><span class="js-path-segment"><a data-pjax="true" href="/clberube/BISIP/tree/master/bisip"><span>bisip</span></a></span><span class="separator">/</span><strong class="final-path">GUI.py</strong>
      </h2>

      <div class="BtnGroup flex-shrink-0 d-none d-md-inline-block">
        <a href="/clberube/BISIP/find/master"
              class="js-pjax-capture-input btn btn-sm BtnGroup-item"
              data-pjax
              data-hotkey="t">
          Find file
        </a>
        <clipboard-copy value="bisip/GUI.py" class="btn btn-sm BtnGroup-item">
          Copy path
        </clipboard-copy>
      </div>
    </div>



    
  <div class="Box Box--condensed d-flex flex-column flex-shrink-0">
      <div class="Box-body d-flex flex-justify-between bg-blue-light flex-column flex-md-row flex-items-start flex-md-items-center">
        <span class="pr-md-4 f6">
          <a rel="author" data-skip-pjax="true" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=20193582" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/clberube"><img class="avatar" src="https://avatars0.githubusercontent.com/u/20193582?s=40&amp;v=4" width="20" height="20" alt="@clberube" /></a>
          <a class="text-bold link-gray-dark lh-default v-align-middle" rel="author" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=20193582" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/clberube">clberube</a>
            <span class="lh-default v-align-middle">
              <a data-pjax="true" title="fixed preview data" class="link-gray" href="/clberube/BISIP/commit/726c9d806e1843e4d9939a936883ea622b22f2b9">fixed preview data</a>
            </span>
        </span>
        <span class="d-inline-block flex-shrink-0 v-align-bottom f6 mt-2 mt-md-0">
          <a class="pr-2 text-mono link-gray" href="/clberube/BISIP/commit/726c9d806e1843e4d9939a936883ea622b22f2b9" data-pjax>726c9d8</a>
          <relative-time datetime="2018-03-22T22:12:50Z">Mar 22, 2018</relative-time>
        </span>
      </div>

    <div class="Box-body d-flex flex-items-center flex-auto f6 border-bottom-0 flex-wrap" >
      <details class="details-reset details-overlay details-overlay-dark lh-default text-gray-dark float-left mr-2" id="blob_contributors_box">
        <summary class="btn-link" aria-haspopup="dialog">
          <span><strong>1</strong> contributor</span>
        </summary>
        <details-dialog
          class="Box Box--overlay d-flex flex-column anim-fade-in fast"
          aria-label="Users who have contributed to this file"
          src="/clberube/BISIP/contributors/master/bisip/GUI.py/list" preload>
          <div class="Box-header">
            <button class="Box-btn-octicon btn-octicon float-right" type="button" aria-label="Close dialog" data-close-dialog>
              <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
            </button>
            <h3 class="Box-title">
              Users who have contributed to this file
            </h3>
          </div>
          <include-fragment class="octocat-spinner my-3" aria-label="Loading..."></include-fragment>
        </details-dialog>
      </details>
    </div>
  </div>





    <div class="Box mt-3 position-relative">
      
<div class="Box-header py-2 d-flex flex-column flex-shrink-0 flex-md-row flex-md-items-center">

  <div class="text-mono f6 flex-auto pr-3 flex-order-2 flex-md-order-1 mt-2 mt-md-0">
      1146 lines (1033 sloc)
      <span class="file-info-divider"></span>
    61.2 KB
  </div>

  <div class="d-flex py-1 py-md-0 flex-auto flex-order-1 flex-md-order-2 flex-sm-grow-0 flex-justify-between">

    <div class="BtnGroup">
      <a id="raw-url" class="btn btn-sm BtnGroup-item" href="/clberube/BISIP/raw/master/bisip/GUI.py">Raw</a>
        <a class="btn btn-sm js-update-url-with-hash BtnGroup-item" data-hotkey="b" href="/clberube/BISIP/blame/master/bisip/GUI.py">Blame</a>
      <a rel="nofollow" class="btn btn-sm BtnGroup-item" href="/clberube/BISIP/commits/master/bisip/GUI.py">History</a>
    </div>


    <div>

          <button type="button" class="btn-octicon disabled tooltipped tooltipped-nw"
            aria-label="You must be signed in to make or propose changes">
            <svg class="octicon octicon-pencil" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l1.3-1.3a.996.996 0 0 1 1.41 0l1.59 1.59c.39.39.39 1.02 0 1.41z"/></svg>
          </button>
          <button type="button" class="btn-octicon btn-octicon-danger disabled tooltipped tooltipped-nw"
            aria-label="You must be signed in to make or propose changes">
            <svg class="octicon octicon-trashcan" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11 2H9c0-.55-.45-1-1-1H5c-.55 0-1 .45-1 1H2c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1v9c0 .55.45 1 1 1h7c.55 0 1-.45 1-1V5c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm-1 12H3V5h1v8h1V5h1v8h1V5h1v8h1V5h1v9zm1-10H2V3h9v1z"/></svg>
          </button>
    </div>
  </div>
</div>




      

  <div itemprop="text" class="Box-body p-0 blob-wrapper data type-python ">
      
<table class="highlight tab-size js-file-line-container" data-tab-size="8">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> -*- coding: utf-8 -*-</span></td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code blob-code-inner js-file-line"><span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code blob-code-inner js-file-line"><span class="pl-s">Created on Tue Apr 21 12:05:22 2015</span></td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code blob-code-inner js-file-line"><span class="pl-s">@author:    charleslberube@gmail.com</span></td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code blob-code-inner js-file-line"><span class="pl-s">            École Polytechnique de Montréal</span></td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code blob-code-inner js-file-line"><span class="pl-s">The MIT License (MIT)</span></td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code blob-code-inner js-file-line"><span class="pl-s">Copyright (c) 2015-2016 Charles L. Bérubé</span></td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code blob-code-inner js-file-line"><span class="pl-s">Permission is hereby granted, free of charge, to any person obtaining a copy</span></td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code blob-code-inner js-file-line"><span class="pl-s">of this software and associated documentation files (the &quot;Software&quot;), to deal</span></td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code blob-code-inner js-file-line"><span class="pl-s">in the Software without restriction, including without limitation the rights</span></td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code blob-code-inner js-file-line"><span class="pl-s">to use, copy, modify, merge, publish, distribute, sublicense, and/or sell</span></td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code blob-code-inner js-file-line"><span class="pl-s">copies of the Software, and to permit persons to whom the Software is</span></td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code blob-code-inner js-file-line"><span class="pl-s">furnished to do so, subject to the following conditions:</span></td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code blob-code-inner js-file-line"><span class="pl-s">The above copyright notice and this permission notice shall be included in all</span></td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code blob-code-inner js-file-line"><span class="pl-s">copies or substantial portions of the Software.</span></td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code blob-code-inner js-file-line"><span class="pl-s">THE SOFTWARE IS PROVIDED &quot;AS IS&quot;, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR</span></td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code blob-code-inner js-file-line"><span class="pl-s">IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,</span></td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code blob-code-inner js-file-line"><span class="pl-s">FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE</span></td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code blob-code-inner js-file-line"><span class="pl-s">AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER</span></td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code blob-code-inner js-file-line"><span class="pl-s">LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,</span></td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code blob-code-inner js-file-line"><span class="pl-s">OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE</span></td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code blob-code-inner js-file-line"><span class="pl-s">SOFTWARE.</span></td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code blob-code-inner js-file-line"><span class="pl-s">https://opensource.org/licenses/MIT</span></td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code blob-code-inner js-file-line"><span class="pl-s">https://github.com/clberube/bisip</span></td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code blob-code-inner js-file-line"><span class="pl-s">This python script builds the graphical user interface may be used to call the</span></td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code blob-code-inner js-file-line"><span class="pl-s">Bayesian inversion module of all SIP models (BISIP_models.py)</span></td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code blob-code-inner js-file-line"><span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> <span class="pl-c1">__future__</span> <span class="pl-k">import</span> division</td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> <span class="pl-c1">__future__</span> <span class="pl-k">import</span> print_function</td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>from __future__ import unicode_literals</span></td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>==============================================================================</span></td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> System imports</span></td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> platform <span class="pl-k">import</span> system</td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> sys <span class="pl-k">import</span> version_info</td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>Running Python <span class="pl-c1">%d</span>.<span class="pl-c1">%d</span>.<span class="pl-c1">%d</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>version_info[<span class="pl-c1">0</span>:<span class="pl-c1">3</span>], <span class="pl-s"><span class="pl-pds">&quot;</span>on<span class="pl-pds">&quot;</span></span>, system())</td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\n</span>Future imports<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> future <span class="pl-k">import</span> standard_library</td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code blob-code-inner js-file-line">standard_library.install_aliases()</td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> builtins <span class="pl-k">import</span> <span class="pl-c1">zip</span></td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> builtins <span class="pl-k">import</span> <span class="pl-c1">str</span></td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> builtins <span class="pl-k">import</span> <span class="pl-c1">range</span></td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> past.builtins <span class="pl-k">import</span> <span class="pl-v">basestring</span></td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> builtins <span class="pl-k">import</span> <span class="pl-c1">object</span></td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> past.utils <span class="pl-k">import</span> old_div</td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>System imports<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> sys <span class="pl-k">import</span> stdout</td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code blob-code-inner js-file-line">stdout.flush()</td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> os <span class="pl-k">import</span> getcwd</td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> json <span class="pl-k">import</span> load <span class="pl-k">as</span> jload, dump <span class="pl-k">as</span> jdump</td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> warnings <span class="pl-k">import</span> filterwarnings</td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code blob-code-inner js-file-line">filterwarnings(<span class="pl-s"><span class="pl-pds">&#39;</span>ignore<span class="pl-pds">&#39;</span></span>) <span class="pl-c"><span class="pl-c">#</span> Ignore some tkinter warnings</span></td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>GUI imports<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code blob-code-inner js-file-line"><span class="pl-k">if</span> version_info[<span class="pl-c1">0</span>] <span class="pl-k">&lt;</span> <span class="pl-c1">3</span>:</td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">import</span> Tkinter <span class="pl-k">as</span> tk</td>
      </tr>
      <tr>
        <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">import</span> FixTk <span class="pl-c"><span class="pl-c">#</span> To avoid pyinstaller error</span></td>
      </tr>
      <tr>
        <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-code blob-code-inner js-file-line"><span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">import</span> tkinter <span class="pl-k">as</span> tk</td>
      </tr>
      <tr>
        <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> tkinter.filedialog, tkinter.messagebox, tkinter.font</td>
      </tr>
      <tr>
        <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>BISIP imports<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> bisip.models <span class="pl-k">import</span> mcmcinv</td>
      </tr>
      <tr>
        <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> bisip.invResults <span class="pl-k">as</span> iR</td>
      </tr>
      <tr>
        <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>Other imports<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> matplotlib.backends.backend_tkagg <span class="pl-k">import</span> FigureCanvasTkAgg, NavigationToolbar2TkAgg</td>
      </tr>
      <tr>
        <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> matplotlib.pyplot <span class="pl-k">import</span> rcParams</td>
      </tr>
      <tr>
        <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> itertools <span class="pl-k">import</span> combinations</td>
      </tr>
      <tr>
        <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> collections <span class="pl-k">import</span> OrderedDict</td>
      </tr>
      <tr>
        <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>All modules successfully loaded<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="LC87" class="blob-code blob-code-inner js-file-line"><span class="pl-k">try</span>: </td>
      </tr>
      <tr>
        <td id="L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="LC88" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">import</span> lib_dd.config.cfg_single <span class="pl-k">as</span> cfg_single</td>
      </tr>
      <tr>
        <td id="L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="LC89" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>CCDtools available<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="LC90" class="blob-code blob-code-inner js-file-line"><span class="pl-k">except</span>: </td>
      </tr>
      <tr>
        <td id="L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="LC91" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="LC92" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="LC93" class="blob-code blob-code-inner js-file-line">stdout.flush()</td>
      </tr>
      <tr>
        <td id="L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="LC94" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="LC95" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> matplotlib <span class="pl-k">as</span> mpl</td>
      </tr>
      <tr>
        <td id="L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="LC96" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>mpl.rc_file_defaults()</span></td>
      </tr>
      <tr>
        <td id="L97" class="blob-num js-line-number" data-line-number="97"></td>
        <td id="LC97" class="blob-code blob-code-inner js-file-line">mpl.rcdefaults()</td>
      </tr>
      <tr>
        <td id="L98" class="blob-num js-line-number" data-line-number="98"></td>
        <td id="LC98" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L99" class="blob-num js-line-number" data-line-number="99"></td>
        <td id="LC99" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>==============================================================================</span></td>
      </tr>
      <tr>
        <td id="L100" class="blob-num js-line-number" data-line-number="100"></td>
        <td id="LC100" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Fonts</span></td>
      </tr>
      <tr>
        <td id="L101" class="blob-num js-line-number" data-line-number="101"></td>
        <td id="LC101" class="blob-code blob-code-inner js-file-line"><span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Darwin<span class="pl-pds">&quot;</span></span> <span class="pl-k">in</span> system():</td>
      </tr>
      <tr>
        <td id="L102" class="blob-num js-line-number" data-line-number="102"></td>
        <td id="LC102" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>    print(&quot;\nOS X detected&quot;)</span></td>
      </tr>
      <tr>
        <td id="L103" class="blob-num js-line-number" data-line-number="103"></td>
        <td id="LC103" class="blob-code blob-code-inner js-file-line">    fontsize <span class="pl-k">=</span> <span class="pl-c1">12</span></td>
      </tr>
      <tr>
        <td id="L104" class="blob-num js-line-number" data-line-number="104"></td>
        <td id="LC104" class="blob-code blob-code-inner js-file-line">    pad_radio <span class="pl-k">=</span> <span class="pl-c1">3</span></td>
      </tr>
      <tr>
        <td id="L105" class="blob-num js-line-number" data-line-number="105"></td>
        <td id="LC105" class="blob-code blob-code-inner js-file-line">    but_size <span class="pl-k">=</span> <span class="pl-k">-</span><span class="pl-c1">2</span></td>
      </tr>
      <tr>
        <td id="L106" class="blob-num js-line-number" data-line-number="106"></td>
        <td id="LC106" class="blob-code blob-code-inner js-file-line">    res_size <span class="pl-k">=</span> <span class="pl-k">-</span><span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L107" class="blob-num js-line-number" data-line-number="107"></td>
        <td id="LC107" class="blob-code blob-code-inner js-file-line"><span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L108" class="blob-num js-line-number" data-line-number="108"></td>
        <td id="LC108" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>    print(&quot;\nWindows detected&quot;)</span></td>
      </tr>
      <tr>
        <td id="L109" class="blob-num js-line-number" data-line-number="109"></td>
        <td id="LC109" class="blob-code blob-code-inner js-file-line">    fontsize <span class="pl-k">=</span> <span class="pl-c1">10</span></td>
      </tr>
      <tr>
        <td id="L110" class="blob-num js-line-number" data-line-number="110"></td>
        <td id="LC110" class="blob-code blob-code-inner js-file-line">    pad_radio <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L111" class="blob-num js-line-number" data-line-number="111"></td>
        <td id="LC111" class="blob-code blob-code-inner js-file-line">    but_size <span class="pl-k">=</span> <span class="pl-k">-</span><span class="pl-c1">2</span></td>
      </tr>
      <tr>
        <td id="L112" class="blob-num js-line-number" data-line-number="112"></td>
        <td id="LC112" class="blob-code blob-code-inner js-file-line">    res_size <span class="pl-k">=</span> <span class="pl-k">-</span><span class="pl-c1">2</span></td>
      </tr>
      <tr>
        <td id="L113" class="blob-num js-line-number" data-line-number="113"></td>
        <td id="LC113" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L114" class="blob-num js-line-number" data-line-number="114"></td>
        <td id="LC114" class="blob-code blob-code-inner js-file-line">window_font <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>TkDefaultFont <span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>fontsize</td>
      </tr>
      <tr>
        <td id="L115" class="blob-num js-line-number" data-line-number="115"></td>
        <td id="LC115" class="blob-code blob-code-inner js-file-line">fontz <span class="pl-k">=</span> {<span class="pl-s"><span class="pl-pds">&quot;</span>bold<span class="pl-pds">&quot;</span></span>: (<span class="pl-s"><span class="pl-pds">&quot;</span>TkDefaultFont<span class="pl-pds">&quot;</span></span>, fontsize, <span class="pl-s"><span class="pl-pds">&quot;</span>bold<span class="pl-pds">&quot;</span></span>),</td>
      </tr>
      <tr>
        <td id="L116" class="blob-num js-line-number" data-line-number="116"></td>
        <td id="LC116" class="blob-code blob-code-inner js-file-line">         <span class="pl-s"><span class="pl-pds">&quot;</span>normal_small<span class="pl-pds">&quot;</span></span>: (<span class="pl-s"><span class="pl-pds">&quot;</span>TkDefaultFont<span class="pl-pds">&quot;</span></span>, fontsize<span class="pl-k">+</span>but_size, <span class="pl-s"><span class="pl-pds">&quot;</span>normal<span class="pl-pds">&quot;</span></span>),</td>
      </tr>
      <tr>
        <td id="L117" class="blob-num js-line-number" data-line-number="117"></td>
        <td id="LC117" class="blob-code blob-code-inner js-file-line">         <span class="pl-s"><span class="pl-pds">&quot;</span>italic_small<span class="pl-pds">&quot;</span></span>: (<span class="pl-s"><span class="pl-pds">&quot;</span>TkDefaultFont<span class="pl-pds">&quot;</span></span>, fontsize<span class="pl-k">+</span>but_size, <span class="pl-s"><span class="pl-pds">&quot;</span>italic<span class="pl-pds">&quot;</span></span>)}</td>
      </tr>
      <tr>
        <td id="L118" class="blob-num js-line-number" data-line-number="118"></td>
        <td id="LC118" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L119" class="blob-num js-line-number" data-line-number="119"></td>
        <td id="LC119" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> To flatten ND lists</span></td>
      </tr>
      <tr>
        <td id="L120" class="blob-num js-line-number" data-line-number="120"></td>
        <td id="LC120" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">flatten</span>(<span class="pl-smi">x</span>):</td>
      </tr>
      <tr>
        <td id="L121" class="blob-num js-line-number" data-line-number="121"></td>
        <td id="LC121" class="blob-code blob-code-inner js-file-line">    result <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L122" class="blob-num js-line-number" data-line-number="122"></td>
        <td id="LC122" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> el <span class="pl-k">in</span> x:</td>
      </tr>
      <tr>
        <td id="L123" class="blob-num js-line-number" data-line-number="123"></td>
        <td id="LC123" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">hasattr</span>(el, <span class="pl-s"><span class="pl-pds">&quot;</span>__iter__<span class="pl-pds">&quot;</span></span>) <span class="pl-k">and</span> <span class="pl-k">not</span> <span class="pl-c1">isinstance</span>(el, <span class="pl-v">basestring</span>):</td>
      </tr>
      <tr>
        <td id="L124" class="blob-num js-line-number" data-line-number="124"></td>
        <td id="LC124" class="blob-code blob-code-inner js-file-line">            result.extend(flatten(el))</td>
      </tr>
      <tr>
        <td id="L125" class="blob-num js-line-number" data-line-number="125"></td>
        <td id="LC125" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L126" class="blob-num js-line-number" data-line-number="126"></td>
        <td id="LC126" class="blob-code blob-code-inner js-file-line">            result.append(el)</td>
      </tr>
      <tr>
        <td id="L127" class="blob-num js-line-number" data-line-number="127"></td>
        <td id="LC127" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> result</td>
      </tr>
      <tr>
        <td id="L128" class="blob-num js-line-number" data-line-number="128"></td>
        <td id="LC128" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L129" class="blob-num js-line-number" data-line-number="129"></td>
        <td id="LC129" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>==============================================================================</span></td>
      </tr>
      <tr>
        <td id="L130" class="blob-num js-line-number" data-line-number="130"></td>
        <td id="LC130" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Import last used window parameters</span></td>
      </tr>
      <tr>
        <td id="L131" class="blob-num js-line-number" data-line-number="131"></td>
        <td id="LC131" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> All GUI options and choices saved when closing the main window</span></td>
      </tr>
      <tr>
        <td id="L132" class="blob-num js-line-number" data-line-number="132"></td>
        <td id="LC132" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Parameters are saved in root_ini file in the executable&#39;s directory</span></td>
      </tr>
      <tr>
        <td id="L133" class="blob-num js-line-number" data-line-number="133"></td>
        <td id="LC133" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> To reset and use default parameters, delete root_ini in local directory</span></td>
      </tr>
      <tr>
        <td id="L134" class="blob-num js-line-number" data-line-number="134"></td>
        <td id="LC134" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L135" class="blob-num js-line-number" data-line-number="135"></td>
        <td id="LC135" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">MainApplication</span>(<span class="pl-c1">object</span>):</td>
      </tr>
      <tr>
        <td id="L136" class="blob-num js-line-number" data-line-number="136"></td>
        <td id="LC136" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>    working_path = str(osp_realpath(argv[0])).replace(&quot;\\&quot;, &quot;/&quot;)+&quot;/&quot;</span></td>
      </tr>
      <tr>
        <td id="L137" class="blob-num js-line-number" data-line-number="137"></td>
        <td id="LC137" class="blob-code blob-code-inner js-file-line">    working_path <span class="pl-k">=</span> getcwd().replace(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\\</span><span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>/<span class="pl-pds">&quot;</span></span>)<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span>/<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L138" class="blob-num js-line-number" data-line-number="138"></td>
        <td id="LC138" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-c1">__init__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">master</span>, <span class="pl-smi">fontz</span>):</td>
      </tr>
      <tr>
        <td id="L139" class="blob-num js-line-number" data-line-number="139"></td>
        <td id="LC139" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.save_options <span class="pl-k">=</span> {<span class="pl-s"><span class="pl-pds">&quot;</span>Save all hexbins (will make error)<span class="pl-pds">&quot;</span></span>:            tk.BooleanVar(),</td>
      </tr>
      <tr>
        <td id="L140" class="blob-num js-line-number" data-line-number="140"></td>
        <td id="LC140" class="blob-code blob-code-inner js-file-line">                             <span class="pl-s"><span class="pl-pds">&quot;</span>Save all bivariate KDE (will make error)<span class="pl-pds">&quot;</span></span>:      tk.BooleanVar(),</td>
      </tr>
      <tr>
        <td id="L141" class="blob-num js-line-number" data-line-number="141"></td>
        <td id="LC141" class="blob-code blob-code-inner js-file-line">                             <span class="pl-s"><span class="pl-pds">&quot;</span>Save fit figures<span class="pl-pds">&quot;</span></span>:            tk.BooleanVar(),</td>
      </tr>
      <tr>
        <td id="L142" class="blob-num js-line-number" data-line-number="142"></td>
        <td id="LC142" class="blob-code blob-code-inner js-file-line">                             <span class="pl-s"><span class="pl-pds">&quot;</span>Save traces figure<span class="pl-pds">&quot;</span></span>:          tk.BooleanVar(),</td>
      </tr>
      <tr>
        <td id="L143" class="blob-num js-line-number" data-line-number="143"></td>
        <td id="LC143" class="blob-code blob-code-inner js-file-line">                             <span class="pl-s"><span class="pl-pds">&quot;</span>Save histograms<span class="pl-pds">&quot;</span></span>:             tk.BooleanVar(),</td>
      </tr>
      <tr>
        <td id="L144" class="blob-num js-line-number" data-line-number="144"></td>
        <td id="LC144" class="blob-code blob-code-inner js-file-line">                             <span class="pl-s"><span class="pl-pds">&quot;</span>Save autocorrelations<span class="pl-pds">&quot;</span></span>:       tk.BooleanVar(),</td>
      </tr>
      <tr>
        <td id="L145" class="blob-num js-line-number" data-line-number="145"></td>
        <td id="LC145" class="blob-code blob-code-inner js-file-line">                             <span class="pl-s"><span class="pl-pds">&quot;</span>Save Debye RTD<span class="pl-pds">&quot;</span></span>:              tk.BooleanVar(),</td>
      </tr>
      <tr>
        <td id="L146" class="blob-num js-line-number" data-line-number="146"></td>
        <td id="LC146" class="blob-code blob-code-inner js-file-line">                             <span class="pl-s"><span class="pl-pds">&quot;</span>Save summaries<span class="pl-pds">&quot;</span></span>:              tk.BooleanVar(),</td>
      </tr>
      <tr>
        <td id="L147" class="blob-num js-line-number" data-line-number="147"></td>
        <td id="LC147" class="blob-code blob-code-inner js-file-line">                             <span class="pl-s"><span class="pl-pds">&quot;</span>Save deviance<span class="pl-pds">&quot;</span></span>:               tk.BooleanVar(),</td>
      </tr>
      <tr>
        <td id="L148" class="blob-num js-line-number" data-line-number="148"></td>
        <td id="LC148" class="blob-code blob-code-inner js-file-line">                             <span class="pl-s"><span class="pl-pds">&quot;</span>Save loglikelihood<span class="pl-pds">&quot;</span></span>:          tk.BooleanVar(),</td>
      </tr>
      <tr>
        <td id="L149" class="blob-num js-line-number" data-line-number="149"></td>
        <td id="LC149" class="blob-code blob-code-inner js-file-line">                             <span class="pl-s"><span class="pl-pds">&quot;</span>Save traces as txt<span class="pl-pds">&quot;</span></span>:          tk.BooleanVar(),</td>
      </tr>
      <tr>
        <td id="L150" class="blob-num js-line-number" data-line-number="150"></td>
        <td id="LC150" class="blob-code blob-code-inner js-file-line">                             <span class="pl-s"><span class="pl-pds">&quot;</span>Save traces in CSV<span class="pl-pds">&quot;</span></span>:          tk.BooleanVar(),</td>
      </tr>
      <tr>
        <td id="L151" class="blob-num js-line-number" data-line-number="151"></td>
        <td id="LC151" class="blob-code blob-code-inner js-file-line">                             <span class="pl-s"><span class="pl-pds">&quot;</span>Tuning verbose<span class="pl-pds">&quot;</span></span>:              tk.BooleanVar(),</td>
      </tr>
      <tr>
        <td id="L152" class="blob-num js-line-number" data-line-number="152"></td>
        <td id="LC152" class="blob-code blob-code-inner js-file-line">                             <span class="pl-s"><span class="pl-pds">&quot;</span>No subplots<span class="pl-pds">&quot;</span></span>:                 tk.BooleanVar(),</td>
      </tr>
      <tr>
        <td id="L153" class="blob-num js-line-number" data-line-number="153"></td>
        <td id="LC153" class="blob-code blob-code-inner js-file-line">                             <span class="pl-s"><span class="pl-pds">&quot;</span>PNG figures<span class="pl-pds">&quot;</span></span>:                 tk.BooleanVar(),</td>
      </tr>
      <tr>
        <td id="L154" class="blob-num js-line-number" data-line-number="154"></td>
        <td id="LC154" class="blob-code blob-code-inner js-file-line">                            }</td>
      </tr>
      <tr>
        <td id="L155" class="blob-num js-line-number" data-line-number="155"></td>
        <td id="LC155" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.run_options <span class="pl-k">=</span> OrderedDict((</td>
      </tr>
      <tr>
        <td id="L156" class="blob-num js-line-number" data-line-number="156"></td>
        <td id="LC156" class="blob-code blob-code-inner js-file-line">                            (<span class="pl-s"><span class="pl-pds">&quot;</span>Auto draw fit<span class="pl-pds">&quot;</span></span>,                tk.BooleanVar()),</td>
      </tr>
      <tr>
        <td id="L157" class="blob-num js-line-number" data-line-number="157"></td>
        <td id="LC157" class="blob-code blob-code-inner js-file-line">                            (<span class="pl-s"><span class="pl-pds">&quot;</span>Print results in console<span class="pl-pds">&quot;</span></span>,     tk.BooleanVar()),</td>
      </tr>
      <tr>
        <td id="L158" class="blob-num js-line-number" data-line-number="158"></td>
        <td id="LC158" class="blob-code blob-code-inner js-file-line">                            (<span class="pl-s"><span class="pl-pds">&quot;</span>Save CSV results<span class="pl-pds">&quot;</span></span>,             tk.BooleanVar()),</td>
      </tr>
      <tr>
        <td id="L159" class="blob-num js-line-number" data-line-number="159"></td>
        <td id="LC159" class="blob-code blob-code-inner js-file-line">                            ))</td>
      </tr>
      <tr>
        <td id="L160" class="blob-num js-line-number" data-line-number="160"></td>
        <td id="LC160" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L161" class="blob-num js-line-number" data-line-number="161"></td>
        <td id="LC161" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.mcmc_vars <span class="pl-k">=</span> OrderedDict((</td>
      </tr>
      <tr>
        <td id="L162" class="blob-num js-line-number" data-line-number="162"></td>
        <td id="LC162" class="blob-code blob-code-inner js-file-line">                                (<span class="pl-s"><span class="pl-pds">&quot;</span>Number of chains<span class="pl-pds">&quot;</span></span>     , (tk.IntVar(), <span class="pl-c1">1</span>)),</td>
      </tr>
      <tr>
        <td id="L163" class="blob-num js-line-number" data-line-number="163"></td>
        <td id="LC163" class="blob-code blob-code-inner js-file-line">                                (<span class="pl-s"><span class="pl-pds">&quot;</span>Total iterations<span class="pl-pds">&quot;</span></span>     , (tk.IntVar(), <span class="pl-c1">10000</span>)),</td>
      </tr>
      <tr>
        <td id="L164" class="blob-num js-line-number" data-line-number="164"></td>
        <td id="LC164" class="blob-code blob-code-inner js-file-line">                                (<span class="pl-s"><span class="pl-pds">&quot;</span>Burn-in period<span class="pl-pds">&quot;</span></span>       , (tk.IntVar(), <span class="pl-c1">8000</span>)),</td>
      </tr>
      <tr>
        <td id="L165" class="blob-num js-line-number" data-line-number="165"></td>
        <td id="LC165" class="blob-code blob-code-inner js-file-line">                                (<span class="pl-s"><span class="pl-pds">&quot;</span>Thinning factor<span class="pl-pds">&quot;</span></span>      , (tk.IntVar(), <span class="pl-c1">1</span>)),</td>
      </tr>
      <tr>
        <td id="L166" class="blob-num js-line-number" data-line-number="166"></td>
        <td id="LC166" class="blob-code blob-code-inner js-file-line">                                (<span class="pl-s"><span class="pl-pds">&quot;</span>Tuning interval<span class="pl-pds">&quot;</span></span>      , (tk.IntVar(), <span class="pl-c1">1000</span>)),</td>
      </tr>
      <tr>
        <td id="L167" class="blob-num js-line-number" data-line-number="167"></td>
        <td id="LC167" class="blob-code blob-code-inner js-file-line">                                (<span class="pl-s"><span class="pl-pds">&quot;</span>Proposal scale<span class="pl-pds">&quot;</span></span>       , (tk.DoubleVar(), <span class="pl-c1">1</span>)),</td>
      </tr>
      <tr>
        <td id="L168" class="blob-num js-line-number" data-line-number="168"></td>
        <td id="LC168" class="blob-code blob-code-inner js-file-line">                                (<span class="pl-s"><span class="pl-pds">&quot;</span>Covariance delay<span class="pl-pds">&quot;</span></span>     , (tk.IntVar(), <span class="pl-c1">1000</span>)),</td>
      </tr>
      <tr>
        <td id="L169" class="blob-num js-line-number" data-line-number="169"></td>
        <td id="LC169" class="blob-code blob-code-inner js-file-line">                                (<span class="pl-s"><span class="pl-pds">&quot;</span>Covariance interval<span class="pl-pds">&quot;</span></span>  , (tk.IntVar(), <span class="pl-c1">1000</span>)),</td>
      </tr>
      <tr>
        <td id="L170" class="blob-num js-line-number" data-line-number="170"></td>
        <td id="LC170" class="blob-code blob-code-inner js-file-line">                                ))</td>
      </tr>
      <tr>
        <td id="L171" class="blob-num js-line-number" data-line-number="171"></td>
        <td id="LC171" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L172" class="blob-num js-line-number" data-line-number="172"></td>
        <td id="LC172" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.master <span class="pl-k">=</span> master</td>
      </tr>
      <tr>
        <td id="L173" class="blob-num js-line-number" data-line-number="173"></td>
        <td id="LC173" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.master.resizable(<span class="pl-v">width</span><span class="pl-k">=</span>tk.<span class="pl-c1">FALSE</span>, <span class="pl-v">height</span><span class="pl-k">=</span>tk.<span class="pl-c1">FALSE</span>)</td>
      </tr>
      <tr>
        <td id="L174" class="blob-num js-line-number" data-line-number="174"></td>
        <td id="LC174" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.load()</td>
      </tr>
      <tr>
        <td id="L175" class="blob-num js-line-number" data-line-number="175"></td>
        <td id="LC175" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.set_plot_par()</td>
      </tr>
      <tr>
        <td id="L176" class="blob-num js-line-number" data-line-number="176"></td>
        <td id="LC176" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.build_helpmenu()</td>
      </tr>
      <tr>
        <td id="L177" class="blob-num js-line-number" data-line-number="177"></td>
        <td id="LC177" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.make_main_frames()</td>
      </tr>
      <tr>
        <td id="L178" class="blob-num js-line-number" data-line-number="178"></td>
        <td id="LC178" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.make_browse_button()</td>
      </tr>
      <tr>
        <td id="L179" class="blob-num js-line-number" data-line-number="179"></td>
        <td id="LC179" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.headers_input()</td>
      </tr>
      <tr>
        <td id="L180" class="blob-num js-line-number" data-line-number="180"></td>
        <td id="LC180" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.open_files <span class="pl-k">=</span> <span class="pl-c1">self</span>.root_ini[<span class="pl-s"><span class="pl-pds">&quot;</span>Imported files<span class="pl-pds">&quot;</span></span>]</td>
      </tr>
      <tr>
        <td id="L181" class="blob-num js-line-number" data-line-number="181"></td>
        <td id="LC181" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.draw_file_list()</td>
      </tr>
      <tr>
        <td id="L182" class="blob-num js-line-number" data-line-number="182"></td>
        <td id="LC182" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.phase_units()</td>
      </tr>
      <tr>
        <td id="L183" class="blob-num js-line-number" data-line-number="183"></td>
        <td id="LC183" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.mcmc_parameters()</td>
      </tr>
      <tr>
        <td id="L184" class="blob-num js-line-number" data-line-number="184"></td>
        <td id="LC184" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.run_exit()</td>
      </tr>
      <tr>
        <td id="L185" class="blob-num js-line-number" data-line-number="185"></td>
        <td id="LC185" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.make_options(<span class="pl-v">from_root</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L186" class="blob-num js-line-number" data-line-number="186"></td>
        <td id="LC186" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.model_choice()</td>
      </tr>
      <tr>
        <td id="L187" class="blob-num js-line-number" data-line-number="187"></td>
        <td id="LC187" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.activity(<span class="pl-v">idle</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L188" class="blob-num js-line-number" data-line-number="188"></td>
        <td id="LC188" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L189" class="blob-num js-line-number" data-line-number="189"></td>
        <td id="LC189" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">use_default_root_ini</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L190" class="blob-num js-line-number" data-line-number="190"></td>
        <td id="LC190" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.default_root <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L191" class="blob-num js-line-number" data-line-number="191"></td>
        <td id="LC191" class="blob-code blob-code-inner js-file-line">                            <span class="pl-s"><span class="pl-pds">&quot;</span>Spectral IP model<span class="pl-pds">&quot;</span></span>     : <span class="pl-s"><span class="pl-pds">&quot;</span>ColeCole<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L192" class="blob-num js-line-number" data-line-number="192"></td>
        <td id="LC192" class="blob-code blob-code-inner js-file-line">                            <span class="pl-s"><span class="pl-pds">&quot;</span>Adaptive Metropolis<span class="pl-pds">&quot;</span></span>   : <span class="pl-c1">True</span>,</td>
      </tr>
      <tr>
        <td id="L193" class="blob-num js-line-number" data-line-number="193"></td>
        <td id="LC193" class="blob-code blob-code-inner js-file-line">                            <span class="pl-s"><span class="pl-pds">&quot;</span>Nb header lines<span class="pl-pds">&quot;</span></span>       : <span class="pl-c1">1</span>,</td>
      </tr>
      <tr>
        <td id="L194" class="blob-num js-line-number" data-line-number="194"></td>
        <td id="LC194" class="blob-code blob-code-inner js-file-line">                            <span class="pl-s"><span class="pl-pds">&quot;</span>Phase units<span class="pl-pds">&quot;</span></span>           : <span class="pl-s"><span class="pl-pds">&quot;</span>mrad<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L195" class="blob-num js-line-number" data-line-number="195"></td>
        <td id="LC195" class="blob-code blob-code-inner js-file-line">                            <span class="pl-s"><span class="pl-pds">&quot;</span>Imported files<span class="pl-pds">&quot;</span></span>        : [],</td>
      </tr>
      <tr>
        <td id="L196" class="blob-num js-line-number" data-line-number="196"></td>
        <td id="LC196" class="blob-code blob-code-inner js-file-line">                            <span class="pl-s"><span class="pl-pds">&quot;</span>Polyn order<span class="pl-pds">&quot;</span></span>           : <span class="pl-c1">4</span>,</td>
      </tr>
      <tr>
        <td id="L197" class="blob-num js-line-number" data-line-number="197"></td>
        <td id="LC197" class="blob-code blob-code-inner js-file-line">                            <span class="pl-s"><span class="pl-pds">&quot;</span>Freq dep<span class="pl-pds">&quot;</span></span>              : <span class="pl-c1">1.0</span>,</td>
      </tr>
      <tr>
        <td id="L198" class="blob-num js-line-number" data-line-number="198"></td>
        <td id="LC198" class="blob-code blob-code-inner js-file-line">                            <span class="pl-s"><span class="pl-pds">&quot;</span>Nb modes<span class="pl-pds">&quot;</span></span>              : <span class="pl-c1">2</span>,</td>
      </tr>
      <tr>
        <td id="L199" class="blob-num js-line-number" data-line-number="199"></td>
        <td id="LC199" class="blob-code blob-code-inner js-file-line">                            <span class="pl-s"><span class="pl-pds">&quot;</span>Lambda<span class="pl-pds">&quot;</span></span>                : <span class="pl-c1">10</span>,</td>
      </tr>
      <tr>
        <td id="L200" class="blob-num js-line-number" data-line-number="200"></td>
        <td id="LC200" class="blob-code blob-code-inner js-file-line">                            }</td>
      </tr>
      <tr>
        <td id="L201" class="blob-num js-line-number" data-line-number="201"></td>
        <td id="LC201" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> k, v <span class="pl-k">in</span> <span class="pl-c1">list</span>(<span class="pl-c1">self</span>.save_options.items()):</td>
      </tr>
      <tr>
        <td id="L202" class="blob-num js-line-number" data-line-number="202"></td>
        <td id="LC202" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.default_root[k] <span class="pl-k">=</span> v.get()</td>
      </tr>
      <tr>
        <td id="L203" class="blob-num js-line-number" data-line-number="203"></td>
        <td id="LC203" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> k, v <span class="pl-k">in</span> <span class="pl-c1">list</span>(<span class="pl-c1">self</span>.mcmc_vars.items()):</td>
      </tr>
      <tr>
        <td id="L204" class="blob-num js-line-number" data-line-number="204"></td>
        <td id="LC204" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.default_root[k] <span class="pl-k">=</span> v[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L205" class="blob-num js-line-number" data-line-number="205"></td>
        <td id="LC205" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> k, v <span class="pl-k">in</span> <span class="pl-c1">list</span>(<span class="pl-c1">self</span>.run_options.items()):</td>
      </tr>
      <tr>
        <td id="L206" class="blob-num js-line-number" data-line-number="206"></td>
        <td id="LC206" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.default_root[k] <span class="pl-k">=</span> v.get()</td>
      </tr>
      <tr>
        <td id="L207" class="blob-num js-line-number" data-line-number="207"></td>
        <td id="LC207" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">self</span>.default_root</td>
      </tr>
      <tr>
        <td id="L208" class="blob-num js-line-number" data-line-number="208"></td>
        <td id="LC208" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L209" class="blob-num js-line-number" data-line-number="209"></td>
        <td id="LC209" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>==============================================================================</span></td>
      </tr>
      <tr>
        <td id="L210" class="blob-num js-line-number" data-line-number="210"></td>
        <td id="LC210" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Main frames</span></td>
      </tr>
      <tr>
        <td id="L211" class="blob-num js-line-number" data-line-number="211"></td>
        <td id="LC211" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>==============================================================================</span></td>
      </tr>
      <tr>
        <td id="L212" class="blob-num js-line-number" data-line-number="212"></td>
        <td id="LC212" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">make_main_frames</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L213" class="blob-num js-line-number" data-line-number="213"></td>
        <td id="LC213" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> Frame for importing files</span></td>
      </tr>
      <tr>
        <td id="L214" class="blob-num js-line-number" data-line-number="214"></td>
        <td id="LC214" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.frame_import <span class="pl-k">=</span> tk.LabelFrame(<span class="pl-c1">self</span>.master, <span class="pl-v">text</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>1. Import data<span class="pl-pds">&quot;</span></span>, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">200</span>, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">5</span>, <span class="pl-v">font</span><span class="pl-k">=</span>fontz[<span class="pl-s"><span class="pl-pds">&quot;</span>bold<span class="pl-pds">&quot;</span></span>])</td>
      </tr>
      <tr>
        <td id="L215" class="blob-num js-line-number" data-line-number="215"></td>
        <td id="LC215" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.frame_import.grid(<span class="pl-v">row</span> <span class="pl-k">=</span> <span class="pl-c1">0</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">columnspan</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">rowspan</span><span class="pl-k">=</span><span class="pl-c1">5</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W<span class="pl-k">+</span>tk.E<span class="pl-k">+</span>tk.N, <span class="pl-v">padx</span><span class="pl-k">=</span><span class="pl-c1">10</span>, <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">5</span>,<span class="pl-c1">15</span>))</td>
      </tr>
      <tr>
        <td id="L216" class="blob-num js-line-number" data-line-number="216"></td>
        <td id="LC216" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.frame_import.grid_columnconfigure(<span class="pl-c1">0</span>, <span class="pl-v">weight</span><span class="pl-k">=</span><span class="pl-c1">1</span>), <span class="pl-c1">self</span>.frame_import.grid_rowconfigure(<span class="pl-c1">0</span>, <span class="pl-v">weight</span><span class="pl-k">=</span><span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L217" class="blob-num js-line-number" data-line-number="217"></td>
        <td id="LC217" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> Frame for choosing the model</span></td>
      </tr>
      <tr>
        <td id="L218" class="blob-num js-line-number" data-line-number="218"></td>
        <td id="LC218" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.frame_model <span class="pl-k">=</span> tk.LabelFrame(<span class="pl-c1">self</span>.master, <span class="pl-v">text</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>2. SIP model<span class="pl-pds">&quot;</span></span>, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">200</span>, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">4</span>, <span class="pl-v">font</span><span class="pl-k">=</span>fontz[<span class="pl-s"><span class="pl-pds">&quot;</span>bold<span class="pl-pds">&quot;</span></span>])</td>
      </tr>
      <tr>
        <td id="L219" class="blob-num js-line-number" data-line-number="219"></td>
        <td id="LC219" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.frame_model.grid(<span class="pl-v">row</span> <span class="pl-k">=</span> <span class="pl-c1">6</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">columnspan</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W<span class="pl-k">+</span>tk.E<span class="pl-k">+</span>tk.N, <span class="pl-v">padx</span><span class="pl-k">=</span><span class="pl-c1">10</span>, <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">5</span>,<span class="pl-c1">15</span>))</td>
      </tr>
      <tr>
        <td id="L220" class="blob-num js-line-number" data-line-number="220"></td>
        <td id="LC220" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.frame_model.grid_columnconfigure(<span class="pl-c1">0</span>, <span class="pl-v">weight</span><span class="pl-k">=</span><span class="pl-c1">1</span>), <span class="pl-c1">self</span>.frame_model.grid_rowconfigure(<span class="pl-c1">0</span>, <span class="pl-v">weight</span><span class="pl-k">=</span><span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L221" class="blob-num js-line-number" data-line-number="221"></td>
        <td id="LC221" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> Frame to enter mcmc parameters</span></td>
      </tr>
      <tr>
        <td id="L222" class="blob-num js-line-number" data-line-number="222"></td>
        <td id="LC222" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.frame_mcmc <span class="pl-k">=</span> tk.LabelFrame(<span class="pl-c1">self</span>.master, <span class="pl-v">text</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>3. MCMC settings<span class="pl-pds">&quot;</span></span>, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">200</span>, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">4</span>, <span class="pl-v">font</span><span class="pl-k">=</span>fontz[<span class="pl-s"><span class="pl-pds">&quot;</span>bold<span class="pl-pds">&quot;</span></span>])</td>
      </tr>
      <tr>
        <td id="L223" class="blob-num js-line-number" data-line-number="223"></td>
        <td id="LC223" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.frame_mcmc.grid(<span class="pl-v">row</span> <span class="pl-k">=</span> <span class="pl-c1">7</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">columnspan</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W<span class="pl-k">+</span>tk.E<span class="pl-k">+</span>tk.N, <span class="pl-v">padx</span><span class="pl-k">=</span><span class="pl-c1">10</span>, <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">5</span>,<span class="pl-c1">15</span>), <span class="pl-v">ipady</span><span class="pl-k">=</span><span class="pl-c1">3</span>)</td>
      </tr>
      <tr>
        <td id="L224" class="blob-num js-line-number" data-line-number="224"></td>
        <td id="LC224" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.frame_mcmc.grid_columnconfigure(<span class="pl-c1">0</span>, <span class="pl-v">weight</span><span class="pl-k">=</span><span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L225" class="blob-num js-line-number" data-line-number="225"></td>
        <td id="LC225" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> Frame to run and exit</span></td>
      </tr>
      <tr>
        <td id="L226" class="blob-num js-line-number" data-line-number="226"></td>
        <td id="LC226" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.frame_ruex <span class="pl-k">=</span> tk.LabelFrame(<span class="pl-c1">self</span>.master, <span class="pl-v">text</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>4. Run<span class="pl-pds">&quot;</span></span>, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">200</span>, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">4</span>, <span class="pl-v">font</span><span class="pl-k">=</span>fontz[<span class="pl-s"><span class="pl-pds">&quot;</span>bold<span class="pl-pds">&quot;</span></span>])</td>
      </tr>
      <tr>
        <td id="L227" class="blob-num js-line-number" data-line-number="227"></td>
        <td id="LC227" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.frame_ruex.grid(<span class="pl-v">row</span> <span class="pl-k">=</span> <span class="pl-c1">8</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">columnspan</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.S<span class="pl-k">+</span>tk.W<span class="pl-k">+</span>tk.E<span class="pl-k">+</span>tk.N, <span class="pl-v">padx</span><span class="pl-k">=</span><span class="pl-c1">10</span>, <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">5</span>,<span class="pl-c1">10</span>))</td>
      </tr>
      <tr>
        <td id="L228" class="blob-num js-line-number" data-line-number="228"></td>
        <td id="LC228" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.frame_ruex.columnconfigure(<span class="pl-c1">0</span>, <span class="pl-v">weight</span><span class="pl-k">=</span><span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L229" class="blob-num js-line-number" data-line-number="229"></td>
        <td id="LC229" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> Frame to list the imported files and preview</span></td>
      </tr>
      <tr>
        <td id="L230" class="blob-num js-line-number" data-line-number="230"></td>
        <td id="LC230" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.frame_list <span class="pl-k">=</span> tk.LabelFrame(<span class="pl-c1">self</span>.master, <span class="pl-v">text</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>List of imported files<span class="pl-pds">&quot;</span></span>, <span class="pl-v">font</span><span class="pl-k">=</span>fontz[<span class="pl-s"><span class="pl-pds">&quot;</span>bold<span class="pl-pds">&quot;</span></span>])</td>
      </tr>
      <tr>
        <td id="L231" class="blob-num js-line-number" data-line-number="231"></td>
        <td id="LC231" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.frame_list.grid(<span class="pl-v">row</span> <span class="pl-k">=</span> <span class="pl-c1">0</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">columnspan</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">rowspan</span><span class="pl-k">=</span><span class="pl-c1">15</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W<span class="pl-k">+</span>tk.E<span class="pl-k">+</span>tk.N<span class="pl-k">+</span>tk.S, <span class="pl-v">padx</span><span class="pl-k">=</span><span class="pl-c1">10</span>, <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">5</span>,<span class="pl-c1">10</span>))</td>
      </tr>
      <tr>
        <td id="L232" class="blob-num js-line-number" data-line-number="232"></td>
        <td id="LC232" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.frame_list.grid_rowconfigure(<span class="pl-c1">1</span>, <span class="pl-v">weight</span><span class="pl-k">=</span><span class="pl-c1">1</span>), <span class="pl-c1">self</span>.frame_list.columnconfigure(<span class="pl-c1">0</span>, <span class="pl-v">weight</span><span class="pl-k">=</span><span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L233" class="blob-num js-line-number" data-line-number="233"></td>
        <td id="LC233" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> Frame to visualize results</span></td>
      </tr>
      <tr>
        <td id="L234" class="blob-num js-line-number" data-line-number="234"></td>
        <td id="LC234" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.frame_results <span class="pl-k">=</span> tk.LabelFrame(<span class="pl-c1">self</span>.master, <span class="pl-v">text</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Results<span class="pl-pds">&quot;</span></span>, <span class="pl-v">font</span><span class="pl-k">=</span>fontz[<span class="pl-s"><span class="pl-pds">&quot;</span>bold<span class="pl-pds">&quot;</span></span>])</td>
      </tr>
      <tr>
        <td id="L235" class="blob-num js-line-number" data-line-number="235"></td>
        <td id="LC235" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.frame_results.grid(<span class="pl-v">row</span> <span class="pl-k">=</span> <span class="pl-c1">0</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">2</span>, <span class="pl-v">columnspan</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">rowspan</span><span class="pl-k">=</span><span class="pl-c1">15</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W<span class="pl-k">+</span>tk.E<span class="pl-k">+</span>tk.N<span class="pl-k">+</span>tk.S, <span class="pl-v">padx</span><span class="pl-k">=</span><span class="pl-c1">10</span>, <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">5</span>,<span class="pl-c1">10</span>))</td>
      </tr>
      <tr>
        <td id="L236" class="blob-num js-line-number" data-line-number="236"></td>
        <td id="LC236" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.frame_results.grid_rowconfigure(<span class="pl-c1">14</span>, <span class="pl-v">weight</span><span class="pl-k">=</span><span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L237" class="blob-num js-line-number" data-line-number="237"></td>
        <td id="LC237" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L238" class="blob-num js-line-number" data-line-number="238"></td>
        <td id="LC238" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>==============================================================================</span></td>
      </tr>
      <tr>
        <td id="L239" class="blob-num js-line-number" data-line-number="239"></td>
        <td id="LC239" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Running inversion</span></td>
      </tr>
      <tr>
        <td id="L240" class="blob-num js-line-number" data-line-number="240"></td>
        <td id="LC240" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>==============================================================================</span></td>
      </tr>
      <tr>
        <td id="L241" class="blob-num js-line-number" data-line-number="241"></td>
        <td id="LC241" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">run_inversion</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L242" class="blob-num js-line-number" data-line-number="242"></td>
        <td id="LC242" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:    <span class="pl-c1">self</span>.clear()</td>
      </tr>
      <tr>
        <td id="L243" class="blob-num js-line-number" data-line-number="243"></td>
        <td id="LC243" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span>: <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L244" class="blob-num js-line-number" data-line-number="244"></td>
        <td id="LC244" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.sel_files <span class="pl-k">=</span> [<span class="pl-c1">str</span>(<span class="pl-c1">self</span>.open_files[i]) <span class="pl-k">for</span> i <span class="pl-k">in</span> <span class="pl-c1">self</span>.text_files.curselection()]</td>
      </tr>
      <tr>
        <td id="L245" class="blob-num js-line-number" data-line-number="245"></td>
        <td id="LC245" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">len</span>(<span class="pl-c1">self</span>.sel_files) <span class="pl-k">==</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L246" class="blob-num js-line-number" data-line-number="246"></td>
        <td id="LC246" class="blob-code blob-code-inner js-file-line">            tkinter.messagebox.showwarning(<span class="pl-s"><span class="pl-pds">&quot;</span>Inversion error<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L247" class="blob-num js-line-number" data-line-number="247"></td>
        <td id="LC247" class="blob-code blob-code-inner js-file-line">                                     <span class="pl-s"><span class="pl-pds">&quot;</span>No data selected for inversion <span class="pl-cce">\n</span>Select at least one data file in the left panel<span class="pl-pds">&quot;</span></span>, <span class="pl-v">parent</span><span class="pl-k">=</span><span class="pl-c1">self</span>.master)</td>
      </tr>
      <tr>
        <td id="L248" class="blob-num js-line-number" data-line-number="248"></td>
        <td id="LC248" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">len</span>(<span class="pl-c1">self</span>.sel_files) <span class="pl-k">&gt;=</span> <span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L249" class="blob-num js-line-number" data-line-number="249"></td>
        <td id="LC249" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L250" class="blob-num js-line-number" data-line-number="250"></td>
        <td id="LC250" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.Inversion()</td>
      </tr>
      <tr>
        <td id="L251" class="blob-num js-line-number" data-line-number="251"></td>
        <td id="LC251" class="blob-code blob-code-inner js-file-line">                stdout.flush()</td>
      </tr>
      <tr>
        <td id="L252" class="blob-num js-line-number" data-line-number="252"></td>
        <td id="LC252" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L253" class="blob-num js-line-number" data-line-number="253"></td>
        <td id="LC253" class="blob-code blob-code-inner js-file-line">                tkinter.messagebox.showerror(<span class="pl-s"><span class="pl-pds">&quot;</span>Inversion error<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>Error<span class="pl-cce">\n</span>Make sure all fields are OK<span class="pl-cce">\n</span>Make sure data file is correctly formatted<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L254" class="blob-num js-line-number" data-line-number="254"></td>
        <td id="LC254" class="blob-code blob-code-inner js-file-line">                                             <span class="pl-v">parent</span><span class="pl-k">=</span><span class="pl-c1">self</span>.master)</td>
      </tr>
      <tr>
        <td id="L255" class="blob-num js-line-number" data-line-number="255"></td>
        <td id="LC255" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L256" class="blob-num js-line-number" data-line-number="256"></td>
        <td id="LC256" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L257" class="blob-num js-line-number" data-line-number="257"></td>
        <td id="LC257" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">Inversion</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L258" class="blob-num js-line-number" data-line-number="258"></td>
        <td id="LC258" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\n</span><span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L259" class="blob-num js-line-number" data-line-number="259"></td>
        <td id="LC259" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>=====================<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L260" class="blob-num js-line-number" data-line-number="260"></td>
        <td id="LC260" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>Starting inversion...<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L261" class="blob-num js-line-number" data-line-number="261"></td>
        <td id="LC261" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>=====================<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L262" class="blob-num js-line-number" data-line-number="262"></td>
        <td id="LC262" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L263" class="blob-num js-line-number" data-line-number="263"></td>
        <td id="LC263" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>Model:<span class="pl-pds">&quot;</span></span>, <span class="pl-c1">self</span>.model.get())</td>
      </tr>
      <tr>
        <td id="L264" class="blob-num js-line-number" data-line-number="264"></td>
        <td id="LC264" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.model.get() <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>CCD<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L265" class="blob-num js-line-number" data-line-number="265"></td>
        <td id="LC265" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>CCD lambda:<span class="pl-pds">&quot;</span></span>, <span class="pl-c1">self</span>.lamb_da.get())</td>
      </tr>
      <tr>
        <td id="L266" class="blob-num js-line-number" data-line-number="266"></td>
        <td id="LC266" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.model.get() <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>ColeCole<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L267" class="blob-num js-line-number" data-line-number="267"></td>
        <td id="LC267" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>Cole-Cole modes:<span class="pl-pds">&quot;</span></span>, <span class="pl-c1">self</span>.modes_n.get())       </td>
      </tr>
      <tr>
        <td id="L268" class="blob-num js-line-number" data-line-number="268"></td>
        <td id="LC268" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.model.get() <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>PDecomp<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L269" class="blob-num js-line-number" data-line-number="269"></td>
        <td id="LC269" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>Polynomial order:<span class="pl-pds">&quot;</span></span>, <span class="pl-c1">self</span>.poly_n.get())</td>
      </tr>
      <tr>
        <td id="L270" class="blob-num js-line-number" data-line-number="270"></td>
        <td id="LC270" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">self</span>.c_exp.get() <span class="pl-k">==</span> <span class="pl-c1">1.0</span>:</td>
      </tr>
      <tr>
        <td id="L271" class="blob-num js-line-number" data-line-number="271"></td>
        <td id="LC271" class="blob-code blob-code-inner js-file-line">                decomp_type <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>(Debye)<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L272" class="blob-num js-line-number" data-line-number="272"></td>
        <td id="LC272" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">elif</span> <span class="pl-c1">self</span>.c_exp.get() <span class="pl-k">==</span> <span class="pl-c1">0.5</span>:</td>
      </tr>
      <tr>
        <td id="L273" class="blob-num js-line-number" data-line-number="273"></td>
        <td id="LC273" class="blob-code blob-code-inner js-file-line">                decomp_type <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>(Warburg)<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L274" class="blob-num js-line-number" data-line-number="274"></td>
        <td id="LC274" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L275" class="blob-num js-line-number" data-line-number="275"></td>
        <td id="LC275" class="blob-code blob-code-inner js-file-line">                decomp_type <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>(Cole-Cole)<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L276" class="blob-num js-line-number" data-line-number="276"></td>
        <td id="LC276" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>Frequency dependence:<span class="pl-pds">&quot;</span></span>, <span class="pl-c1">self</span>.c_exp.get(), decomp_type)</td>
      </tr>
      <tr>
        <td id="L277" class="blob-num js-line-number" data-line-number="277"></td>
        <td id="LC277" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>Units:<span class="pl-pds">&quot;</span></span>, <span class="pl-c1">self</span>.units.get())</td>
      </tr>
      <tr>
        <td id="L278" class="blob-num js-line-number" data-line-number="278"></td>
        <td id="LC278" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>Paths:<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L279" class="blob-num js-line-number" data-line-number="279"></td>
        <td id="LC279" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> i <span class="pl-k">in</span> <span class="pl-c1">self</span>.sel_files:</td>
      </tr>
      <tr>
        <td id="L280" class="blob-num js-line-number" data-line-number="280"></td>
        <td id="LC280" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span>(i)</td>
      </tr>
      <tr>
        <td id="L281" class="blob-num js-line-number" data-line-number="281"></td>
        <td id="LC281" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>Skipping<span class="pl-pds">&quot;</span></span>, <span class="pl-c1">self</span>.head.get(), <span class="pl-s"><span class="pl-pds">&quot;</span>header lines<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L282" class="blob-num js-line-number" data-line-number="282"></td>
        <td id="LC282" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.files <span class="pl-k">=</span> [<span class="pl-c1">self</span>.sel_files[i].split(<span class="pl-s"><span class="pl-pds">&quot;</span>/<span class="pl-pds">&quot;</span></span>)[<span class="pl-k">-</span><span class="pl-c1">1</span>].split(<span class="pl-s"><span class="pl-pds">&quot;</span>.<span class="pl-pds">&quot;</span></span>)[<span class="pl-c1">0</span>] <span class="pl-k">for</span> i <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-c1">len</span>((<span class="pl-c1">self</span>.sel_files)))]</td>
      </tr>
      <tr>
        <td id="L283" class="blob-num js-line-number" data-line-number="283"></td>
        <td id="LC283" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L284" class="blob-num js-line-number" data-line-number="284"></td>
        <td id="LC284" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.mcmc_params <span class="pl-k">=</span> {<span class="pl-s"><span class="pl-pds">&quot;</span>adaptive<span class="pl-pds">&quot;</span></span>   : <span class="pl-c1">self</span>.adaptive.get(),</td>
      </tr>
      <tr>
        <td id="L285" class="blob-num js-line-number" data-line-number="285"></td>
        <td id="LC285" class="blob-code blob-code-inner js-file-line">                            <span class="pl-s"><span class="pl-pds">&quot;</span>verbose<span class="pl-pds">&quot;</span></span>    : <span class="pl-c1">self</span>.save_options[<span class="pl-s"><span class="pl-pds">&quot;</span>Tuning verbose<span class="pl-pds">&quot;</span></span>].get(),</td>
      </tr>
      <tr>
        <td id="L286" class="blob-num js-line-number" data-line-number="286"></td>
        <td id="LC286" class="blob-code blob-code-inner js-file-line">                            <span class="pl-s"><span class="pl-pds">&quot;</span>nb_chain<span class="pl-pds">&quot;</span></span>   : <span class="pl-c1">self</span>.mcmc_vars[<span class="pl-s"><span class="pl-pds">&quot;</span>Number of chains<span class="pl-pds">&quot;</span></span>][<span class="pl-c1">0</span>].get(),</td>
      </tr>
      <tr>
        <td id="L287" class="blob-num js-line-number" data-line-number="287"></td>
        <td id="LC287" class="blob-code blob-code-inner js-file-line">                            <span class="pl-s"><span class="pl-pds">&quot;</span>nb_iter<span class="pl-pds">&quot;</span></span>    : <span class="pl-c1">self</span>.mcmc_vars[<span class="pl-s"><span class="pl-pds">&quot;</span>Total iterations<span class="pl-pds">&quot;</span></span>][<span class="pl-c1">0</span>].get(),</td>
      </tr>
      <tr>
        <td id="L288" class="blob-num js-line-number" data-line-number="288"></td>
        <td id="LC288" class="blob-code blob-code-inner js-file-line">                            <span class="pl-s"><span class="pl-pds">&quot;</span>nb_burn<span class="pl-pds">&quot;</span></span>    : <span class="pl-c1">self</span>.mcmc_vars[<span class="pl-s"><span class="pl-pds">&quot;</span>Burn-in period<span class="pl-pds">&quot;</span></span>][<span class="pl-c1">0</span>].get(),</td>
      </tr>
      <tr>
        <td id="L289" class="blob-num js-line-number" data-line-number="289"></td>
        <td id="LC289" class="blob-code blob-code-inner js-file-line">                            <span class="pl-s"><span class="pl-pds">&quot;</span>thin<span class="pl-pds">&quot;</span></span>       : <span class="pl-c1">self</span>.mcmc_vars[<span class="pl-s"><span class="pl-pds">&quot;</span>Thinning factor<span class="pl-pds">&quot;</span></span>][<span class="pl-c1">0</span>].get(),</td>
      </tr>
      <tr>
        <td id="L290" class="blob-num js-line-number" data-line-number="290"></td>
        <td id="LC290" class="blob-code blob-code-inner js-file-line">                            <span class="pl-s"><span class="pl-pds">&quot;</span>tune_inter<span class="pl-pds">&quot;</span></span> : <span class="pl-c1">self</span>.mcmc_vars[<span class="pl-s"><span class="pl-pds">&quot;</span>Tuning interval<span class="pl-pds">&quot;</span></span>][<span class="pl-c1">0</span>].get(),</td>
      </tr>
      <tr>
        <td id="L291" class="blob-num js-line-number" data-line-number="291"></td>
        <td id="LC291" class="blob-code blob-code-inner js-file-line">                            <span class="pl-s"><span class="pl-pds">&quot;</span>prop_scale<span class="pl-pds">&quot;</span></span> : <span class="pl-c1">self</span>.mcmc_vars[<span class="pl-s"><span class="pl-pds">&quot;</span>Proposal scale<span class="pl-pds">&quot;</span></span>][<span class="pl-c1">0</span>].get(),</td>
      </tr>
      <tr>
        <td id="L292" class="blob-num js-line-number" data-line-number="292"></td>
        <td id="LC292" class="blob-code blob-code-inner js-file-line">                            <span class="pl-s"><span class="pl-pds">&quot;</span>cov_inter<span class="pl-pds">&quot;</span></span>  : <span class="pl-c1">self</span>.mcmc_vars[<span class="pl-s"><span class="pl-pds">&quot;</span>Covariance interval<span class="pl-pds">&quot;</span></span>][<span class="pl-c1">0</span>].get(),</td>
      </tr>
      <tr>
        <td id="L293" class="blob-num js-line-number" data-line-number="293"></td>
        <td id="LC293" class="blob-code blob-code-inner js-file-line">                            <span class="pl-s"><span class="pl-pds">&quot;</span>cov_delay<span class="pl-pds">&quot;</span></span>  : <span class="pl-c1">self</span>.mcmc_vars[<span class="pl-s"><span class="pl-pds">&quot;</span>Covariance delay<span class="pl-pds">&quot;</span></span>][<span class="pl-c1">0</span>].get(),</td>
      </tr>
      <tr>
        <td id="L294" class="blob-num js-line-number" data-line-number="294"></td>
        <td id="LC294" class="blob-code blob-code-inner js-file-line">                            }</td>
      </tr>
      <tr>
        <td id="L295" class="blob-num js-line-number" data-line-number="295"></td>
        <td id="LC295" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> Appel de la fonction d&#39;inversion avec les paramètres sélectionnés</span></td>
      </tr>
      <tr>
        <td id="L296" class="blob-num js-line-number" data-line-number="296"></td>
        <td id="LC296" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:    <span class="pl-k">del</span>(<span class="pl-c1">self</span>.all_results)</td>
      </tr>
      <tr>
        <td id="L297" class="blob-num js-line-number" data-line-number="297"></td>
        <td id="LC297" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span>: <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L298" class="blob-num js-line-number" data-line-number="298"></td>
        <td id="LC298" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.all_results <span class="pl-k">=</span> {}</td>
      </tr>
      <tr>
        <td id="L299" class="blob-num js-line-number" data-line-number="299"></td>
        <td id="LC299" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.draw_drop_down()</td>
      </tr>
      <tr>
        <td id="L300" class="blob-num js-line-number" data-line-number="300"></td>
        <td id="LC300" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.var_review.set(<span class="pl-s"><span class="pl-pds">&quot;</span>Working...<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L301" class="blob-num js-line-number" data-line-number="301"></td>
        <td id="LC301" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> (i, <span class="pl-c1">self</span>.f_n) <span class="pl-k">in</span> <span class="pl-c1">enumerate</span>(<span class="pl-c1">self</span>.files):</td>
      </tr>
      <tr>
        <td id="L302" class="blob-num js-line-number" data-line-number="302"></td>
        <td id="LC302" class="blob-code blob-code-inner js-file-line">            </td>
      </tr>
      <tr>
        <td id="L303" class="blob-num js-line-number" data-line-number="303"></td>
        <td id="LC303" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">self</span>.model.get() <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>CCD<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L304" class="blob-num js-line-number" data-line-number="304"></td>
        <td id="LC304" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\n</span>Removing data from CCDtools config<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L305" class="blob-num js-line-number" data-line-number="305"></td>
        <td id="LC305" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.ccdt_config <span class="pl-k">=</span> cfg_single.cfg_single()</td>
      </tr>
      <tr>
        <td id="L306" class="blob-num js-line-number" data-line-number="306"></td>
        <td id="LC306" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.ccdt_config[<span class="pl-s"><span class="pl-pds">&#39;</span>fixed_lambda<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-c1">self</span>.lamb_da.get()</td>
      </tr>
      <tr>
        <td id="L307" class="blob-num js-line-number" data-line-number="307"></td>
        <td id="LC307" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.ccdt_config[<span class="pl-s"><span class="pl-pds">&#39;</span>norm<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-c1">10</span>   </td>
      </tr>
      <tr>
        <td id="L308" class="blob-num js-line-number" data-line-number="308"></td>
        <td id="LC308" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L309" class="blob-num js-line-number" data-line-number="309"></td>
        <td id="LC309" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.ccdt_config <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L310" class="blob-num js-line-number" data-line-number="310"></td>
        <td id="LC310" class="blob-code blob-code-inner js-file-line">            </td>
      </tr>
      <tr>
        <td id="L311" class="blob-num js-line-number" data-line-number="311"></td>
        <td id="LC311" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>=====================<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L312" class="blob-num js-line-number" data-line-number="312"></td>
        <td id="LC312" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.activity()</td>
      </tr>
      <tr>
        <td id="L313" class="blob-num js-line-number" data-line-number="313"></td>
        <td id="LC313" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.var_review.set(<span class="pl-c1">self</span>.f_n)</td>
      </tr>
      <tr>
        <td id="L314" class="blob-num js-line-number" data-line-number="314"></td>
        <td id="LC314" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.sol <span class="pl-k">=</span> mcmcinv(<span class="pl-c1">self</span>.model.get(), <span class="pl-c1">self</span>.sel_files[i], </td>
      </tr>
      <tr>
        <td id="L315" class="blob-num js-line-number" data-line-number="315"></td>
        <td id="LC315" class="blob-code blob-code-inner js-file-line">                               <span class="pl-v">mcmc</span> <span class="pl-k">=</span> <span class="pl-c1">self</span>.mcmc_params,</td>
      </tr>
      <tr>
        <td id="L316" class="blob-num js-line-number" data-line-number="316"></td>
        <td id="LC316" class="blob-code blob-code-inner js-file-line">                               <span class="pl-v">headers</span><span class="pl-k">=</span><span class="pl-c1">self</span>.head.get(), </td>
      </tr>
      <tr>
        <td id="L317" class="blob-num js-line-number" data-line-number="317"></td>
        <td id="LC317" class="blob-code blob-code-inner js-file-line">                               <span class="pl-v">ph_units</span><span class="pl-k">=</span><span class="pl-c1">self</span>.units.get(),</td>
      </tr>
      <tr>
        <td id="L318" class="blob-num js-line-number" data-line-number="318"></td>
        <td id="LC318" class="blob-code blob-code-inner js-file-line">                               <span class="pl-v">cc_modes</span><span class="pl-k">=</span><span class="pl-c1">self</span>.modes_n.get(), </td>
      </tr>
      <tr>
        <td id="L319" class="blob-num js-line-number" data-line-number="319"></td>
        <td id="LC319" class="blob-code blob-code-inner js-file-line">                               <span class="pl-v">decomp_poly</span><span class="pl-k">=</span><span class="pl-c1">self</span>.poly_n.get(),</td>
      </tr>
      <tr>
        <td id="L320" class="blob-num js-line-number" data-line-number="320"></td>
        <td id="LC320" class="blob-code blob-code-inner js-file-line">                               <span class="pl-v">c_exp</span><span class="pl-k">=</span><span class="pl-c1">self</span>.c_exp.get(), </td>
      </tr>
      <tr>
        <td id="L321" class="blob-num js-line-number" data-line-number="321"></td>
        <td id="LC321" class="blob-code blob-code-inner js-file-line">                               <span class="pl-v">keep_traces</span><span class="pl-k">=</span><span class="pl-c1">self</span>.save_options[<span class="pl-s"><span class="pl-pds">&quot;</span>Save traces as txt<span class="pl-pds">&quot;</span></span>].get(),</td>
      </tr>
      <tr>
        <td id="L322" class="blob-num js-line-number" data-line-number="322"></td>
        <td id="LC322" class="blob-code blob-code-inner js-file-line">                               <span class="pl-v">ccdt_priors</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>auto<span class="pl-pds">&#39;</span></span>, </td>
      </tr>
      <tr>
        <td id="L323" class="blob-num js-line-number" data-line-number="323"></td>
        <td id="LC323" class="blob-code blob-code-inner js-file-line">                               <span class="pl-v">ccdt_cfg</span><span class="pl-k">=</span><span class="pl-c1">self</span>.ccdt_config,</td>
      </tr>
      <tr>
        <td id="L324" class="blob-num js-line-number" data-line-number="324"></td>
        <td id="LC324" class="blob-code blob-code-inner js-file-line">                               )</td>
      </tr>
      <tr>
        <td id="L325" class="blob-num js-line-number" data-line-number="325"></td>
        <td id="LC325" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>            print(self.model.get(), self.sel_files[i])</span></td>
      </tr>
      <tr>
        <td id="L326" class="blob-num js-line-number" data-line-number="326"></td>
        <td id="LC326" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.all_results[<span class="pl-c1">self</span>.f_n] <span class="pl-k">=</span> {<span class="pl-s"><span class="pl-pds">&quot;</span>pm<span class="pl-pds">&quot;</span></span>:<span class="pl-c1">self</span>.sol.pm,<span class="pl-s"><span class="pl-pds">&quot;</span>MDL<span class="pl-pds">&quot;</span></span>:<span class="pl-c1">self</span>.sol.<span class="pl-c1">MDL</span>,<span class="pl-s"><span class="pl-pds">&quot;</span>data<span class="pl-pds">&quot;</span></span>:<span class="pl-c1">self</span>.sol.data,<span class="pl-s"><span class="pl-pds">&quot;</span>fit<span class="pl-pds">&quot;</span></span>:<span class="pl-c1">self</span>.sol.fit, <span class="pl-s"><span class="pl-pds">&quot;</span>sol<span class="pl-pds">&quot;</span></span>:<span class="pl-c1">self</span>.sol}</td>
      </tr>
      <tr>
        <td id="L327" class="blob-num js-line-number" data-line-number="327"></td>
        <td id="LC327" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>           Impression ou non des résultats, graphiques, histogrammes</span></td>
      </tr>
      <tr>
        <td id="L328" class="blob-num js-line-number" data-line-number="328"></td>
        <td id="LC328" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">try</span>:            </td>
      </tr>
      <tr>
        <td id="L329" class="blob-num js-line-number" data-line-number="329"></td>
        <td id="LC329" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.update_results()        </td>
      </tr>
      <tr>
        <td id="L330" class="blob-num js-line-number" data-line-number="330"></td>
        <td id="LC330" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L331" class="blob-num js-line-number" data-line-number="331"></td>
        <td id="LC331" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>PROBLEM<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L332" class="blob-num js-line-number" data-line-number="332"></td>
        <td id="LC332" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">self</span>.run_options[<span class="pl-s"><span class="pl-pds">&quot;</span>Print results in console<span class="pl-pds">&quot;</span></span>].get():</td>
      </tr>
      <tr>
        <td id="L333" class="blob-num js-line-number" data-line-number="333"></td>
        <td id="LC333" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.sol.print_results()</td>
      </tr>
      <tr>
        <td id="L334" class="blob-num js-line-number" data-line-number="334"></td>
        <td id="LC334" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">self</span>.run_options[<span class="pl-s"><span class="pl-pds">&quot;</span>Save CSV results<span class="pl-pds">&quot;</span></span>].get():</td>
      </tr>
      <tr>
        <td id="L335" class="blob-num js-line-number" data-line-number="335"></td>
        <td id="LC335" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.sol.save_results()</td>
      </tr>
      <tr>
        <td id="L336" class="blob-num js-line-number" data-line-number="336"></td>
        <td id="LC336" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">self</span>.save_options[<span class="pl-s"><span class="pl-pds">&quot;</span>Save traces in CSV<span class="pl-pds">&quot;</span></span>].get():</td>
      </tr>
      <tr>
        <td id="L337" class="blob-num js-line-number" data-line-number="337"></td>
        <td id="LC337" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.sol.save_csv_traces()</td>
      </tr>
      <tr>
        <td id="L338" class="blob-num js-line-number" data-line-number="338"></td>
        <td id="LC338" class="blob-code blob-code-inner js-file-line">                </td>
      </tr>
      <tr>
        <td id="L339" class="blob-num js-line-number" data-line-number="339"></td>
        <td id="LC339" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">self</span>.save_options[<span class="pl-s"><span class="pl-pds">&quot;</span>Save fit figures<span class="pl-pds">&quot;</span></span>].get():</td>
      </tr>
      <tr>
        <td id="L340" class="blob-num js-line-number" data-line-number="340"></td>
        <td id="LC340" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.sol.plot_fit(<span class="pl-v">save</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">save_as_png</span><span class="pl-k">=</span><span class="pl-c1">self</span>.save_options[<span class="pl-s"><span class="pl-pds">&quot;</span>PNG figures<span class="pl-pds">&quot;</span></span>].get(), <span class="pl-v">draw</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L341" class="blob-num js-line-number" data-line-number="341"></td>
        <td id="LC341" class="blob-code blob-code-inner js-file-line">            </td>
      </tr>
      <tr>
        <td id="L342" class="blob-num js-line-number" data-line-number="342"></td>
        <td id="LC342" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">self</span>.run_options[<span class="pl-s"><span class="pl-pds">&quot;</span>Auto draw fit<span class="pl-pds">&quot;</span></span>].get():</td>
      </tr>
      <tr>
        <td id="L343" class="blob-num js-line-number" data-line-number="343"></td>
        <td id="LC343" class="blob-code blob-code-inner js-file-line">                fig_fit <span class="pl-k">=</span> <span class="pl-c1">self</span>.sol.plot_fit(<span class="pl-v">save</span><span class="pl-k">=</span><span class="pl-c1">False</span>, <span class="pl-v">draw</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L344" class="blob-num js-line-number" data-line-number="344"></td>
        <td id="LC344" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.plot_window(fig_fit, <span class="pl-s"><span class="pl-pds">&quot;</span>Inversion results: <span class="pl-pds">&quot;</span></span><span class="pl-k">+</span><span class="pl-c1">self</span>.f_n)</td>
      </tr>
      <tr>
        <td id="L345" class="blob-num js-line-number" data-line-number="345"></td>
        <td id="LC345" class="blob-code blob-code-inner js-file-line">                </td>
      </tr>
      <tr>
        <td id="L346" class="blob-num js-line-number" data-line-number="346"></td>
        <td id="LC346" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">self</span>.model.get() <span class="pl-k">in</span> [<span class="pl-s"><span class="pl-pds">&quot;</span>PDecomp<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>CCD<span class="pl-pds">&quot;</span></span>]:</td>
      </tr>
      <tr>
        <td id="L347" class="blob-num js-line-number" data-line-number="347"></td>
        <td id="LC347" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> <span class="pl-c1">self</span>.save_options[<span class="pl-s"><span class="pl-pds">&quot;</span>Save Debye RTD<span class="pl-pds">&quot;</span></span>].get():</td>
      </tr>
      <tr>
        <td id="L348" class="blob-num js-line-number" data-line-number="348"></td>
        <td id="LC348" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">self</span>.sol.plot_rtd(<span class="pl-v">save</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">save_as_png</span><span class="pl-k">=</span><span class="pl-c1">self</span>.save_options[<span class="pl-s"><span class="pl-pds">&quot;</span>PNG figures<span class="pl-pds">&quot;</span></span>].get(), <span class="pl-v">draw</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L349" class="blob-num js-line-number" data-line-number="349"></td>
        <td id="LC349" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">self</span>.save_options[<span class="pl-s"><span class="pl-pds">&quot;</span>Save all hexbins (will make error)<span class="pl-pds">&quot;</span></span>].get():</td>
      </tr>
      <tr>
        <td id="L350" class="blob-num js-line-number" data-line-number="350"></td>
        <td id="LC350" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">for</span> v1, v2 <span class="pl-k">in</span> <span class="pl-c1">list</span>(combinations(<span class="pl-c1">self</span>.list_of_parameters, <span class="pl-c1">2</span>)):</td>
      </tr>
      <tr>
        <td id="L351" class="blob-num js-line-number" data-line-number="351"></td>
        <td id="LC351" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">self</span>.all_results[<span class="pl-c1">self</span>.f_n][<span class="pl-s"><span class="pl-pds">&quot;</span>sol<span class="pl-pds">&quot;</span></span>].plot_hexbin(v1, v2, <span class="pl-v">save</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">save_as_png</span><span class="pl-k">=</span><span class="pl-c1">self</span>.save_options[<span class="pl-s"><span class="pl-pds">&quot;</span>PNG figures<span class="pl-pds">&quot;</span></span>].get())</td>
      </tr>
      <tr>
        <td id="L352" class="blob-num js-line-number" data-line-number="352"></td>
        <td id="LC352" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">self</span>.save_options[<span class="pl-s"><span class="pl-pds">&quot;</span>Save all bivariate KDE (will make error)<span class="pl-pds">&quot;</span></span>].get():</td>
      </tr>
      <tr>
        <td id="L353" class="blob-num js-line-number" data-line-number="353"></td>
        <td id="LC353" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">for</span> v1, v2 <span class="pl-k">in</span> <span class="pl-c1">list</span>(combinations(<span class="pl-c1">self</span>.list_of_parameters, <span class="pl-c1">2</span>)):</td>
      </tr>
      <tr>
        <td id="L354" class="blob-num js-line-number" data-line-number="354"></td>
        <td id="LC354" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">self</span>.all_results[<span class="pl-c1">self</span>.f_n][<span class="pl-s"><span class="pl-pds">&quot;</span>sol<span class="pl-pds">&quot;</span></span>].plot_KDE(v1, v2, <span class="pl-v">save</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">save_as_png</span><span class="pl-k">=</span><span class="pl-c1">self</span>.save_options[<span class="pl-s"><span class="pl-pds">&quot;</span>PNG figures<span class="pl-pds">&quot;</span></span>].get())</td>
      </tr>
      <tr>
        <td id="L355" class="blob-num js-line-number" data-line-number="355"></td>
        <td id="LC355" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">self</span>.save_options[<span class="pl-s"><span class="pl-pds">&quot;</span>Save histograms<span class="pl-pds">&quot;</span></span>].get():</td>
      </tr>
      <tr>
        <td id="L356" class="blob-num js-line-number" data-line-number="356"></td>
        <td id="LC356" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">self</span>.all_results[<span class="pl-c1">self</span>.f_n][<span class="pl-s"><span class="pl-pds">&quot;</span>sol<span class="pl-pds">&quot;</span></span>].plot_histograms(<span class="pl-v">no_subplots</span><span class="pl-k">=</span><span class="pl-c1">self</span>.save_options[<span class="pl-s"><span class="pl-pds">&quot;</span>No subplots<span class="pl-pds">&quot;</span></span>].get(), <span class="pl-v">save</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">save_as_png</span><span class="pl-k">=</span><span class="pl-c1">self</span>.save_options[<span class="pl-s"><span class="pl-pds">&quot;</span>PNG figures<span class="pl-pds">&quot;</span></span>].get())</td>
      </tr>
      <tr>
        <td id="L357" class="blob-num js-line-number" data-line-number="357"></td>
        <td id="LC357" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">self</span>.save_options[<span class="pl-s"><span class="pl-pds">&quot;</span>Save traces figure<span class="pl-pds">&quot;</span></span>].get():</td>
      </tr>
      <tr>
        <td id="L358" class="blob-num js-line-number" data-line-number="358"></td>
        <td id="LC358" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.all_results[<span class="pl-c1">self</span>.f_n][<span class="pl-s"><span class="pl-pds">&quot;</span>sol<span class="pl-pds">&quot;</span></span>].plot_traces(<span class="pl-v">no_subplots</span><span class="pl-k">=</span><span class="pl-c1">self</span>.save_options[<span class="pl-s"><span class="pl-pds">&quot;</span>No subplots<span class="pl-pds">&quot;</span></span>].get(), <span class="pl-v">save</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">save_as_png</span><span class="pl-k">=</span><span class="pl-c1">self</span>.save_options[<span class="pl-s"><span class="pl-pds">&quot;</span>PNG figures<span class="pl-pds">&quot;</span></span>].get())</td>
      </tr>
      <tr>
        <td id="L359" class="blob-num js-line-number" data-line-number="359"></td>
        <td id="LC359" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">self</span>.save_options[<span class="pl-s"><span class="pl-pds">&quot;</span>Save summaries<span class="pl-pds">&quot;</span></span>].get():</td>
      </tr>
      <tr>
        <td id="L360" class="blob-num js-line-number" data-line-number="360"></td>
        <td id="LC360" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L361" class="blob-num js-line-number" data-line-number="361"></td>
        <td id="LC361" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">self</span>.all_results[<span class="pl-c1">self</span>.f_n][<span class="pl-s"><span class="pl-pds">&quot;</span>sol<span class="pl-pds">&quot;</span></span>].plot_summary(<span class="pl-v">save</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">save_as_png</span><span class="pl-k">=</span><span class="pl-c1">self</span>.save_options[<span class="pl-s"><span class="pl-pds">&quot;</span>PNG figures<span class="pl-pds">&quot;</span></span>].get())</td>
      </tr>
      <tr>
        <td id="L362" class="blob-num js-line-number" data-line-number="362"></td>
        <td id="LC362" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L363" class="blob-num js-line-number" data-line-number="363"></td>
        <td id="LC363" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\n</span>Error plotting summary: need more than 1 chain for Gelman-Rubin stats<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L364" class="blob-num js-line-number" data-line-number="364"></td>
        <td id="LC364" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">self</span>.save_options[<span class="pl-s"><span class="pl-pds">&quot;</span>Save autocorrelations<span class="pl-pds">&quot;</span></span>].get():</td>
      </tr>
      <tr>
        <td id="L365" class="blob-num js-line-number" data-line-number="365"></td>
        <td id="LC365" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.all_results[<span class="pl-c1">self</span>.f_n][<span class="pl-s"><span class="pl-pds">&quot;</span>sol<span class="pl-pds">&quot;</span></span>].plot_autocorrelation(<span class="pl-v">save</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">save_as_png</span><span class="pl-k">=</span><span class="pl-c1">self</span>.save_options[<span class="pl-s"><span class="pl-pds">&quot;</span>PNG figures<span class="pl-pds">&quot;</span></span>].get())</td>
      </tr>
      <tr>
        <td id="L366" class="blob-num js-line-number" data-line-number="366"></td>
        <td id="LC366" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">self</span>.save_options[<span class="pl-s"><span class="pl-pds">&quot;</span>Save deviance<span class="pl-pds">&quot;</span></span>].get():</td>
      </tr>
      <tr>
        <td id="L367" class="blob-num js-line-number" data-line-number="367"></td>
        <td id="LC367" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.all_results[<span class="pl-c1">self</span>.f_n][<span class="pl-s"><span class="pl-pds">&quot;</span>sol<span class="pl-pds">&quot;</span></span>].plot_model_deviance(<span class="pl-v">save</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">save_as_png</span><span class="pl-k">=</span><span class="pl-c1">self</span>.save_options[<span class="pl-s"><span class="pl-pds">&quot;</span>PNG figures<span class="pl-pds">&quot;</span></span>].get())</td>
      </tr>
      <tr>
        <td id="L368" class="blob-num js-line-number" data-line-number="368"></td>
        <td id="LC368" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">self</span>.save_options[<span class="pl-s"><span class="pl-pds">&quot;</span>Save loglikelihood<span class="pl-pds">&quot;</span></span>].get():</td>
      </tr>
      <tr>
        <td id="L369" class="blob-num js-line-number" data-line-number="369"></td>
        <td id="LC369" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.all_results[<span class="pl-c1">self</span>.f_n][<span class="pl-s"><span class="pl-pds">&quot;</span>sol<span class="pl-pds">&quot;</span></span>].plot_log_likelihood(<span class="pl-v">save</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">save_as_png</span><span class="pl-k">=</span><span class="pl-c1">self</span>.save_options[<span class="pl-s"><span class="pl-pds">&quot;</span>PNG figures<span class="pl-pds">&quot;</span></span>].get())</td>
      </tr>
      <tr>
        <td id="L370" class="blob-num js-line-number" data-line-number="370"></td>
        <td id="LC370" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>            </span></td>
      </tr>
      <tr>
        <td id="L371" class="blob-num js-line-number" data-line-number="371"></td>
        <td id="LC371" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">self</span>.files.index(<span class="pl-c1">self</span>.f_n)<span class="pl-k">+</span><span class="pl-c1">1</span> <span class="pl-k">==</span> <span class="pl-c1">len</span>(<span class="pl-c1">self</span>.files):</td>
      </tr>
      <tr>
        <td id="L372" class="blob-num js-line-number" data-line-number="372"></td>
        <td id="LC372" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.activity(<span class="pl-v">done</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L373" class="blob-num js-line-number" data-line-number="373"></td>
        <td id="LC373" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.diagn_buttons()</td>
      </tr>
      <tr>
        <td id="L374" class="blob-num js-line-number" data-line-number="374"></td>
        <td id="LC374" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.write_output_path()</td>
      </tr>
      <tr>
        <td id="L375" class="blob-num js-line-number" data-line-number="375"></td>
        <td id="LC375" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>=====================<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L376" class="blob-num js-line-number" data-line-number="376"></td>
        <td id="LC376" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L377" class="blob-num js-line-number" data-line-number="377"></td>
        <td id="LC377" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>==============================================================================</span></td>
      </tr>
      <tr>
        <td id="L378" class="blob-num js-line-number" data-line-number="378"></td>
        <td id="LC378" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Result frame</span></td>
      </tr>
      <tr>
        <td id="L379" class="blob-num js-line-number" data-line-number="379"></td>
        <td id="LC379" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>==============================================================================</span></td>
      </tr>
      <tr>
        <td id="L380" class="blob-num js-line-number" data-line-number="380"></td>
        <td id="LC380" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Batch progress</span></td>
      </tr>
      <tr>
        <td id="L381" class="blob-num js-line-number" data-line-number="381"></td>
        <td id="LC381" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">activity</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">idle</span><span class="pl-k">=</span><span class="pl-c1">False</span>, <span class="pl-smi">done</span><span class="pl-k">=</span><span class="pl-c1">False</span>):</td>
      </tr>
      <tr>
        <td id="L382" class="blob-num js-line-number" data-line-number="382"></td>
        <td id="LC382" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:    <span class="pl-c1">self</span>.frame_activ.destroy()</td>
      </tr>
      <tr>
        <td id="L383" class="blob-num js-line-number" data-line-number="383"></td>
        <td id="LC383" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span>: <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L384" class="blob-num js-line-number" data-line-number="384"></td>
        <td id="LC384" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.frame_activ <span class="pl-k">=</span> tk.Frame(<span class="pl-c1">self</span>.frame_results)</td>
      </tr>
      <tr>
        <td id="L385" class="blob-num js-line-number" data-line-number="385"></td>
        <td id="LC385" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.frame_activ.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.E<span class="pl-k">+</span>tk.W, <span class="pl-v">padx</span><span class="pl-k">=</span><span class="pl-c1">10</span>, <span class="pl-v">pady</span><span class="pl-k">=</span><span class="pl-c1">10</span>)</td>
      </tr>
      <tr>
        <td id="L386" class="blob-num js-line-number" data-line-number="386"></td>
        <td id="LC386" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> idle:</td>
      </tr>
      <tr>
        <td id="L387" class="blob-num js-line-number" data-line-number="387"></td>
        <td id="LC387" class="blob-code blob-code-inner js-file-line">            display <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span> <span class="pl-cce">\n</span> <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L388" class="blob-num js-line-number" data-line-number="388"></td>
        <td id="LC388" class="blob-code blob-code-inner js-file-line">            text_act <span class="pl-k">=</span> tk.Label(<span class="pl-c1">self</span>.frame_activ, <span class="pl-v">text</span><span class="pl-k">=</span>display, <span class="pl-v">anchor</span><span class="pl-k">=</span>tk.W, <span class="pl-v">justify</span><span class="pl-k">=</span>tk.<span class="pl-c1">LEFT</span>, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">40</span>)</td>
      </tr>
      <tr>
        <td id="L389" class="blob-num js-line-number" data-line-number="389"></td>
        <td id="LC389" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L390" class="blob-num js-line-number" data-line-number="390"></td>
        <td id="LC390" class="blob-code blob-code-inner js-file-line">            display <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Working on:<span class="pl-cce">\n</span><span class="pl-c1">%s</span> (#<span class="pl-c1">%d</span>/<span class="pl-c1">%d</span>)...<span class="pl-pds">&quot;&quot;&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">self</span>.f_n, <span class="pl-c1">self</span>.files.index(<span class="pl-c1">self</span>.f_n)<span class="pl-k">+</span><span class="pl-c1">1</span>, <span class="pl-c1">len</span>(<span class="pl-c1">self</span>.files))</td>
      </tr>
      <tr>
        <td id="L391" class="blob-num js-line-number" data-line-number="391"></td>
        <td id="LC391" class="blob-code blob-code-inner js-file-line">            text_act <span class="pl-k">=</span> tk.Label(<span class="pl-c1">self</span>.frame_activ, <span class="pl-v">text</span><span class="pl-k">=</span>display, <span class="pl-v">anchor</span><span class="pl-k">=</span>tk.W, <span class="pl-v">justify</span><span class="pl-k">=</span>tk.<span class="pl-c1">LEFT</span>, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">40</span>)</td>
      </tr>
      <tr>
        <td id="L392" class="blob-num js-line-number" data-line-number="392"></td>
        <td id="LC392" class="blob-code blob-code-inner js-file-line">        text_act.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W<span class="pl-k">+</span>tk.E<span class="pl-k">+</span>tk.N)</td>
      </tr>
      <tr>
        <td id="L393" class="blob-num js-line-number" data-line-number="393"></td>
        <td id="LC393" class="blob-code blob-code-inner js-file-line">        text_act.update()</td>
      </tr>
      <tr>
        <td id="L394" class="blob-num js-line-number" data-line-number="394"></td>
        <td id="LC394" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> done:</td>
      </tr>
      <tr>
        <td id="L395" class="blob-num js-line-number" data-line-number="395"></td>
        <td id="LC395" class="blob-code blob-code-inner js-file-line">            text_act.destroy()</td>
      </tr>
      <tr>
        <td id="L396" class="blob-num js-line-number" data-line-number="396"></td>
        <td id="LC396" class="blob-code blob-code-inner js-file-line">            text_done <span class="pl-k">=</span> tk.Label(<span class="pl-c1">self</span>.frame_activ, <span class="pl-v">text</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Done<span class="pl-cce">\n</span><span class="pl-pds">&quot;&quot;&quot;</span></span>, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">40</span>, <span class="pl-v">anchor</span><span class="pl-k">=</span>tk.W)</td>
      </tr>
      <tr>
        <td id="L397" class="blob-num js-line-number" data-line-number="397"></td>
        <td id="LC397" class="blob-code blob-code-inner js-file-line">            text_done.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W<span class="pl-k">+</span>tk.E<span class="pl-k">+</span>tk.N)</td>
      </tr>
      <tr>
        <td id="L398" class="blob-num js-line-number" data-line-number="398"></td>
        <td id="LC398" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L399" class="blob-num js-line-number" data-line-number="399"></td>
        <td id="LC399" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">clear</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">menu</span><span class="pl-k">=</span><span class="pl-c1">False</span>): <span class="pl-c"><span class="pl-c">#</span> self expl</span></td>
      </tr>
      <tr>
        <td id="L400" class="blob-num js-line-number" data-line-number="400"></td>
        <td id="LC400" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.frame_optimal.destroy()</td>
      </tr>
      <tr>
        <td id="L401" class="blob-num js-line-number" data-line-number="401"></td>
        <td id="LC401" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.frame_saved_in.destroy()</td>
      </tr>
      <tr>
        <td id="L402" class="blob-num js-line-number" data-line-number="402"></td>
        <td id="LC402" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.frame_diagn_but.destroy()</td>
      </tr>
      <tr>
        <td id="L403" class="blob-num js-line-number" data-line-number="403"></td>
        <td id="LC403" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> menu:</td>
      </tr>
      <tr>
        <td id="L404" class="blob-num js-line-number" data-line-number="404"></td>
        <td id="LC404" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.frame_drop.destroy(), <span class="pl-c1">self</span>.frame_activ.destroy()</td>
      </tr>
      <tr>
        <td id="L405" class="blob-num js-line-number" data-line-number="405"></td>
        <td id="LC405" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L406" class="blob-num js-line-number" data-line-number="406"></td>
        <td id="LC406" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">change_file</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L407" class="blob-num js-line-number" data-line-number="407"></td>
        <td id="LC407" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.clear()</td>
      </tr>
      <tr>
        <td id="L408" class="blob-num js-line-number" data-line-number="408"></td>
        <td id="LC408" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.update_results()</td>
      </tr>
      <tr>
        <td id="L409" class="blob-num js-line-number" data-line-number="409"></td>
        <td id="LC409" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.diagn_buttons()</td>
      </tr>
      <tr>
        <td id="L410" class="blob-num js-line-number" data-line-number="410"></td>
        <td id="LC410" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.write_output_path()</td>
      </tr>
      <tr>
        <td id="L411" class="blob-num js-line-number" data-line-number="411"></td>
        <td id="LC411" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L412" class="blob-num js-line-number" data-line-number="412"></td>
        <td id="LC412" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">draw_drop_down</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L413" class="blob-num js-line-number" data-line-number="413"></td>
        <td id="LC413" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:    <span class="pl-c1">self</span>.frame_drop.destroy()</td>
      </tr>
      <tr>
        <td id="L414" class="blob-num js-line-number" data-line-number="414"></td>
        <td id="LC414" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span>: <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L415" class="blob-num js-line-number" data-line-number="415"></td>
        <td id="LC415" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.frame_drop <span class="pl-k">=</span> tk.Frame(<span class="pl-c1">self</span>.frame_results)</td>
      </tr>
      <tr>
        <td id="L416" class="blob-num js-line-number" data-line-number="416"></td>
        <td id="LC416" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.frame_drop.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.E<span class="pl-k">+</span>tk.W, <span class="pl-v">padx</span><span class="pl-k">=</span><span class="pl-c1">10</span>, <span class="pl-v">pady</span><span class="pl-k">=</span><span class="pl-c1">3</span>)</td>
      </tr>
      <tr>
        <td id="L417" class="blob-num js-line-number" data-line-number="417"></td>
        <td id="LC417" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.frame_drop.columnconfigure(<span class="pl-c1">0</span>,<span class="pl-v">weight</span><span class="pl-k">=</span><span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L418" class="blob-num js-line-number" data-line-number="418"></td>
        <td id="LC418" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.var_review <span class="pl-k">=</span> tk.StringVar()</td>
      </tr>
      <tr>
        <td id="L419" class="blob-num js-line-number" data-line-number="419"></td>
        <td id="LC419" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.var_review.set(<span class="pl-c1">self</span>.files[<span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L420" class="blob-num js-line-number" data-line-number="420"></td>
        <td id="LC420" class="blob-code blob-code-inner js-file-line">        optionmenu <span class="pl-k">=</span> tk.OptionMenu(<span class="pl-c1">self</span>.frame_drop, <span class="pl-c1">self</span>.var_review, <span class="pl-k">*</span><span class="pl-c1">self</span>.files, <span class="pl-v">command</span> <span class="pl-k">=</span> <span class="pl-k">lambda</span> <span class="pl-smi">x</span>: <span class="pl-c1">self</span>.change_file())</td>
      </tr>
      <tr>
        <td id="L421" class="blob-num js-line-number" data-line-number="421"></td>
        <td id="LC421" class="blob-code blob-code-inner js-file-line">        optionmenu.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W<span class="pl-k">+</span>tk.E<span class="pl-k">+</span>tk.S)</td>
      </tr>
      <tr>
        <td id="L422" class="blob-num js-line-number" data-line-number="422"></td>
        <td id="LC422" class="blob-code blob-code-inner js-file-line">        optionmenu.config(<span class="pl-v">bg</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>gray97<span class="pl-pds">&quot;</span></span>, <span class="pl-v">relief</span><span class="pl-k">=</span>tk.<span class="pl-c1">GROOVE</span>)</td>
      </tr>
      <tr>
        <td id="L423" class="blob-num js-line-number" data-line-number="423"></td>
        <td id="LC423" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L424" class="blob-num js-line-number" data-line-number="424"></td>
        <td id="LC424" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">merge_csv_files</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L425" class="blob-num js-line-number" data-line-number="425"></td>
        <td id="LC425" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">len</span>(<span class="pl-c1">self</span>.files) <span class="pl-k">&gt;</span> <span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L426" class="blob-num js-line-number" data-line-number="426"></td>
        <td id="LC426" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.sol.merge_results(<span class="pl-c1">self</span>.files)</td>
      </tr>
      <tr>
        <td id="L427" class="blob-num js-line-number" data-line-number="427"></td>
        <td id="LC427" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>=====================<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L428" class="blob-num js-line-number" data-line-number="428"></td>
        <td id="LC428" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L429" class="blob-num js-line-number" data-line-number="429"></td>
        <td id="LC429" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>Can&#39;t merge csv files: Only 1 file inverted in last batch<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L430" class="blob-num js-line-number" data-line-number="430"></td>
        <td id="LC430" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>=====================<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L431" class="blob-num js-line-number" data-line-number="431"></td>
        <td id="LC431" class="blob-code blob-code-inner js-file-line">        stdout.flush()</td>
      </tr>
      <tr>
        <td id="L432" class="blob-num js-line-number" data-line-number="432"></td>
        <td id="LC432" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L433" class="blob-num js-line-number" data-line-number="433"></td>
        <td id="LC433" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">RLD_diagnostic</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L434" class="blob-num js-line-number" data-line-number="434"></td>
        <td id="LC434" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">MDL</span> <span class="pl-k">=</span> <span class="pl-c1">self</span>.all_results[<span class="pl-c1">self</span>.var_review.get()][<span class="pl-s"><span class="pl-pds">&quot;</span>MDL<span class="pl-pds">&quot;</span></span>]</td>
      </tr>
      <tr>
        <td id="L435" class="blob-num js-line-number" data-line-number="435"></td>
        <td id="LC435" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.model.get() <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>PDecomp<span class="pl-pds">&quot;</span></span>: adj <span class="pl-k">=</span> <span class="pl-k">-</span><span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L436" class="blob-num js-line-number" data-line-number="436"></td>
        <td id="LC436" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>: adj <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L437" class="blob-num js-line-number" data-line-number="437"></td>
        <td id="LC437" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L438" class="blob-num js-line-number" data-line-number="438"></td>
        <td id="LC438" class="blob-code blob-code-inner js-file-line">            keys <span class="pl-k">=</span> [x.<span class="pl-c1">__name__</span> <span class="pl-k">for</span> x <span class="pl-k">in</span> <span class="pl-c1">MDL</span>.stochastics]</td>
      </tr>
      <tr>
        <td id="L439" class="blob-num js-line-number" data-line-number="439"></td>
        <td id="LC439" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> (i, k) <span class="pl-k">in</span> <span class="pl-c1">enumerate</span>(keys):</td>
      </tr>
      <tr>
        <td id="L440" class="blob-num js-line-number" data-line-number="440"></td>
        <td id="LC440" class="blob-code blob-code-inner js-file-line">                vect <span class="pl-k">=</span> old_div((<span class="pl-c1">MDL</span>.trace(k)[:].size),(<span class="pl-c1">len</span>(<span class="pl-c1">MDL</span>.trace(k)[:])))</td>
      </tr>
      <tr>
        <td id="L441" class="blob-num js-line-number" data-line-number="441"></td>
        <td id="LC441" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> vect <span class="pl-k">&gt;</span> <span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L442" class="blob-num js-line-number" data-line-number="442"></td>
        <td id="LC442" class="blob-code blob-code-inner js-file-line">                 keys[i] <span class="pl-k">=</span> [k<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">%d</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>n <span class="pl-k">for</span> n <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-c1">1</span><span class="pl-k">+</span>adj,vect<span class="pl-k">+</span><span class="pl-c1">1</span><span class="pl-k">+</span>adj)]</td>
      </tr>
      <tr>
        <td id="L443" class="blob-num js-line-number" data-line-number="443"></td>
        <td id="LC443" class="blob-code blob-code-inner js-file-line">            keys <span class="pl-k">=</span> <span class="pl-c1">list</span>(<span class="pl-c1">reversed</span>(<span class="pl-c1">sorted</span>(flatten(keys))))</td>
      </tr>
      <tr>
        <td id="L444" class="blob-num js-line-number" data-line-number="444"></td>
        <td id="LC444" class="blob-code blob-code-inner js-file-line">            top_RLD <span class="pl-k">=</span> tk.Toplevel()</td>
      </tr>
      <tr>
        <td id="L445" class="blob-num js-line-number" data-line-number="445"></td>
        <td id="LC445" class="blob-code blob-code-inner js-file-line">            top_RLD.title(<span class="pl-s"><span class="pl-pds">&quot;</span>Raftery-Lewis diagnostic<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L446" class="blob-num js-line-number" data-line-number="446"></td>
        <td id="LC446" class="blob-code blob-code-inner js-file-line">            text_RLD <span class="pl-k">=</span> tk.Text(top_RLD, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">110</span>, <span class="pl-v">font</span><span class="pl-k">=</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>courier<span class="pl-pds">&#39;</span></span>, fontsize, <span class="pl-s"><span class="pl-pds">&#39;</span>normal<span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="L447" class="blob-num js-line-number" data-line-number="447"></td>
        <td id="LC447" class="blob-code blob-code-inner js-file-line">            text_RLD.grid(<span class="pl-v">stick</span><span class="pl-k">=</span>tk.N, <span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">20</span>,<span class="pl-c1">0</span>), <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">10</span>,<span class="pl-c1">10</span>))</td>
      </tr>
      <tr>
        <td id="L448" class="blob-num js-line-number" data-line-number="448"></td>
        <td id="LC448" class="blob-code blob-code-inner js-file-line">            q<span class="pl-k">=</span><span class="pl-c1">0.025</span></td>
      </tr>
      <tr>
        <td id="L449" class="blob-num js-line-number" data-line-number="449"></td>
        <td id="LC449" class="blob-code blob-code-inner js-file-line">            r<span class="pl-k">=</span><span class="pl-c1">0.01</span></td>
      </tr>
      <tr>
        <td id="L450" class="blob-num js-line-number" data-line-number="450"></td>
        <td id="LC450" class="blob-code blob-code-inner js-file-line">            s<span class="pl-k">=</span><span class="pl-c1">0.95</span></td>
      </tr>
      <tr>
        <td id="L451" class="blob-num js-line-number" data-line-number="451"></td>
        <td id="LC451" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> k <span class="pl-k">in</span> keys:</td>
      </tr>
      <tr>
        <td id="L452" class="blob-num js-line-number" data-line-number="452"></td>
        <td id="LC452" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> k[<span class="pl-k">-</span><span class="pl-c1">1</span>] <span class="pl-k">not</span> <span class="pl-k">in</span> [<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">%d</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>d <span class="pl-k">for</span> d <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-c1">1</span><span class="pl-k">+</span>adj,<span class="pl-c1">8</span>)] <span class="pl-k">or</span> k <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>R0<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L453" class="blob-num js-line-number" data-line-number="453"></td>
        <td id="LC453" class="blob-code blob-code-inner js-file-line">                    data <span class="pl-k">=</span> <span class="pl-c1">MDL</span>.trace(k)[:].ravel()</td>
      </tr>
      <tr>
        <td id="L454" class="blob-num js-line-number" data-line-number="454"></td>
        <td id="LC454" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L455" class="blob-num js-line-number" data-line-number="455"></td>
        <td id="LC455" class="blob-code blob-code-inner js-file-line">                    data <span class="pl-k">=</span> <span class="pl-c1">MDL</span>.trace(k[:<span class="pl-k">-</span><span class="pl-c1">1</span>])[:][:,<span class="pl-c1">int</span>(k[<span class="pl-k">-</span><span class="pl-c1">1</span>])<span class="pl-k">-</span><span class="pl-c1">1</span><span class="pl-k">-</span>adj].ravel()</td>
      </tr>
      <tr>
        <td id="L456" class="blob-num js-line-number" data-line-number="456"></td>
        <td id="LC456" class="blob-code blob-code-inner js-file-line">                F<span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">%s</span>:<span class="pl-cce">\n</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>k</td>
      </tr>
      <tr>
        <td id="L457" class="blob-num js-line-number" data-line-number="457"></td>
        <td id="LC457" class="blob-code blob-code-inner js-file-line">                nmin, kthin, nburn, nprec, kmind <span class="pl-k">=</span> iR.print_diagn(data, q, r, s)</td>
      </tr>
      <tr>
        <td id="L458" class="blob-num js-line-number" data-line-number="458"></td>
        <td id="LC458" class="blob-code blob-code-inner js-file-line">                A<span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">%s</span> iterations required (assuming independence) to achieve <span class="pl-c1">%s</span> accuracy with <span class="pl-c1">%i</span> percent probability.<span class="pl-cce">\n</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span>(nmin, r, <span class="pl-c1">100</span> <span class="pl-k">*</span> s)</td>
      </tr>
      <tr>
        <td id="L459" class="blob-num js-line-number" data-line-number="459"></td>
        <td id="LC459" class="blob-code blob-code-inner js-file-line">                B<span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Thinning factor of <span class="pl-c1">%i</span> required to produce a first-order Markov chain.<span class="pl-cce">\n</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span>kthin</td>
      </tr>
      <tr>
        <td id="L460" class="blob-num js-line-number" data-line-number="460"></td>
        <td id="LC460" class="blob-code blob-code-inner js-file-line">                C<span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">%i</span> iterations to be discarded at the beginning of the simulation (burn-in).<span class="pl-cce">\n</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span>nburn</td>
      </tr>
      <tr>
        <td id="L461" class="blob-num js-line-number" data-line-number="461"></td>
        <td id="LC461" class="blob-code blob-code-inner js-file-line">                D<span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">%s</span> subsequent iterations required.<span class="pl-cce">\n</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span>nprec</td>
      </tr>
      <tr>
        <td id="L462" class="blob-num js-line-number" data-line-number="462"></td>
        <td id="LC462" class="blob-code blob-code-inner js-file-line">                E<span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Thinning factor of <span class="pl-c1">%i</span> required to produce an independence chain.<span class="pl-cce">\n\n</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span>kmind</td>
      </tr>
      <tr>
        <td id="L463" class="blob-num js-line-number" data-line-number="463"></td>
        <td id="LC463" class="blob-code blob-code-inner js-file-line">                text_RLD.insert(<span class="pl-s"><span class="pl-pds">&quot;</span>1.0<span class="pl-pds">&quot;</span></span>, F<span class="pl-k">+</span>A<span class="pl-k">+</span>B<span class="pl-k">+</span>C<span class="pl-k">+</span>D<span class="pl-k">+</span>E)</td>
      </tr>
      <tr>
        <td id="L464" class="blob-num js-line-number" data-line-number="464"></td>
        <td id="LC464" class="blob-code blob-code-inner js-file-line">            text_RLD.insert(<span class="pl-s"><span class="pl-pds">&quot;</span>1.0<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>(From PYMC)<span class="pl-pds">&quot;</span></span><span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\n\n</span><span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L465" class="blob-num js-line-number" data-line-number="465"></td>
        <td id="LC465" class="blob-code blob-code-inner js-file-line">            text_RLD.insert(<span class="pl-s"><span class="pl-pds">&quot;</span>1.0<span class="pl-pds">&quot;</span></span>, <span class="pl-c1">self</span>.var_review.get()<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\n\n</span><span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L466" class="blob-num js-line-number" data-line-number="466"></td>
        <td id="LC466" class="blob-code blob-code-inner js-file-line">            button <span class="pl-k">=</span> tk.Button(top_RLD, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">20</span>, <span class="pl-v">text</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Dismiss<span class="pl-pds">&quot;</span></span>, <span class="pl-v">command</span><span class="pl-k">=</span>top_RLD.destroy, <span class="pl-v">bg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>gray97<span class="pl-pds">&#39;</span></span>, <span class="pl-v">relief</span><span class="pl-k">=</span>tk.<span class="pl-c1">GROOVE</span>)</td>
      </tr>
      <tr>
        <td id="L467" class="blob-num js-line-number" data-line-number="467"></td>
        <td id="LC467" class="blob-code blob-code-inner js-file-line">            button.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.S, <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">0</span>,<span class="pl-c1">10</span>))</td>
      </tr>
      <tr>
        <td id="L468" class="blob-num js-line-number" data-line-number="468"></td>
        <td id="LC468" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L469" class="blob-num js-line-number" data-line-number="469"></td>
        <td id="LC469" class="blob-code blob-code-inner js-file-line">            s <span class="pl-k">=</span> tk.Scrollbar(top_RLD, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">20</span>)</td>
      </tr>
      <tr>
        <td id="L470" class="blob-num js-line-number" data-line-number="470"></td>
        <td id="LC470" class="blob-code blob-code-inner js-file-line">            s.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.E<span class="pl-k">+</span>tk.N<span class="pl-k">+</span>tk.S, <span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">0</span>,<span class="pl-c1">0</span>), <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">10</span>,<span class="pl-c1">10</span>))</td>
      </tr>
      <tr>
        <td id="L471" class="blob-num js-line-number" data-line-number="471"></td>
        <td id="LC471" class="blob-code blob-code-inner js-file-line">            s[<span class="pl-s"><span class="pl-pds">&#39;</span>command<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> text_RLD.yview</td>
      </tr>
      <tr>
        <td id="L472" class="blob-num js-line-number" data-line-number="472"></td>
        <td id="LC472" class="blob-code blob-code-inner js-file-line">            text_RLD[<span class="pl-s"><span class="pl-pds">&#39;</span>yscrollcommand<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> s.set</td>
      </tr>
      <tr>
        <td id="L473" class="blob-num js-line-number" data-line-number="473"></td>
        <td id="LC473" class="blob-code blob-code-inner js-file-line">            top_RLD.resizable(<span class="pl-v">width</span><span class="pl-k">=</span>tk.<span class="pl-c1">FALSE</span>, <span class="pl-v">height</span><span class="pl-k">=</span>tk.<span class="pl-c1">FALSE</span>)</td>
      </tr>
      <tr>
        <td id="L474" class="blob-num js-line-number" data-line-number="474"></td>
        <td id="LC474" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L475" class="blob-num js-line-number" data-line-number="475"></td>
        <td id="LC475" class="blob-code blob-code-inner js-file-line">            tkinter.messagebox.showwarning(<span class="pl-s"><span class="pl-pds">&quot;</span>Diagnostic error<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L476" class="blob-num js-line-number" data-line-number="476"></td>
        <td id="LC476" class="blob-code blob-code-inner js-file-line">                                     <span class="pl-s"><span class="pl-pds">&quot;</span>Error<span class="pl-cce">\n</span>Run inversion first<span class="pl-pds">&quot;</span></span>, <span class="pl-v">parent</span><span class="pl-k">=</span><span class="pl-c1">self</span>.master)</td>
      </tr>
      <tr>
        <td id="L477" class="blob-num js-line-number" data-line-number="477"></td>
        <td id="LC477" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L478" class="blob-num js-line-number" data-line-number="478"></td>
        <td id="LC478" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">popup_bivar</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">bivar_type</span>):</td>
      </tr>
      <tr>
        <td id="L479" class="blob-num js-line-number" data-line-number="479"></td>
        <td id="LC479" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>: <span class="pl-c1">self</span>.top_bivar.destroy()</td>
      </tr>
      <tr>
        <td id="L480" class="blob-num js-line-number" data-line-number="480"></td>
        <td id="LC480" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span>: <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L481" class="blob-num js-line-number" data-line-number="481"></td>
        <td id="LC481" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.top_bivar <span class="pl-k">=</span> tk.Toplevel()</td>
      </tr>
      <tr>
        <td id="L482" class="blob-num js-line-number" data-line-number="482"></td>
        <td id="LC482" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.top_bivar.title(<span class="pl-s"><span class="pl-pds">&quot;</span>Bivariate plotting<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L483" class="blob-num js-line-number" data-line-number="483"></td>
        <td id="LC483" class="blob-code blob-code-inner js-file-line">        tk.Label(<span class="pl-c1">self</span>.top_bivar, <span class="pl-v">text</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Select two different parameters: <span class="pl-pds">&quot;</span></span>).grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W<span class="pl-k">+</span>tk.E<span class="pl-k">+</span>tk.N, <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">5</span>,<span class="pl-c1">5</span>))</td>
      </tr>
      <tr>
        <td id="L484" class="blob-num js-line-number" data-line-number="484"></td>
        <td id="LC484" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.biv1, <span class="pl-c1">self</span>.biv2 <span class="pl-k">=</span> tk.StringVar(), tk.StringVar()</td>
      </tr>
      <tr>
        <td id="L485" class="blob-num js-line-number" data-line-number="485"></td>
        <td id="LC485" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.biv1.set(<span class="pl-c1">self</span>.list_of_parameters[<span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L486" class="blob-num js-line-number" data-line-number="486"></td>
        <td id="LC486" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.biv2.set(<span class="pl-c1">self</span>.list_of_parameters[<span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L487" class="blob-num js-line-number" data-line-number="487"></td>
        <td id="LC487" class="blob-code blob-code-inner js-file-line">        optionmenu1 <span class="pl-k">=</span> tk.OptionMenu(<span class="pl-c1">self</span>.top_bivar, <span class="pl-c1">self</span>.biv1, <span class="pl-k">*</span><span class="pl-c1">self</span>.list_of_parameters)</td>
      </tr>
      <tr>
        <td id="L488" class="blob-num js-line-number" data-line-number="488"></td>
        <td id="LC488" class="blob-code blob-code-inner js-file-line">        optionmenu2 <span class="pl-k">=</span> tk.OptionMenu(<span class="pl-c1">self</span>.top_bivar, <span class="pl-c1">self</span>.biv2, <span class="pl-k">*</span><span class="pl-c1">self</span>.list_of_parameters)</td>
      </tr>
      <tr>
        <td id="L489" class="blob-num js-line-number" data-line-number="489"></td>
        <td id="LC489" class="blob-code blob-code-inner js-file-line">        optionmenu1.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W<span class="pl-k">+</span>tk.E<span class="pl-k">+</span>tk.S)</td>
      </tr>
      <tr>
        <td id="L490" class="blob-num js-line-number" data-line-number="490"></td>
        <td id="LC490" class="blob-code blob-code-inner js-file-line">        optionmenu1.config(<span class="pl-v">bg</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>gray97<span class="pl-pds">&quot;</span></span>, <span class="pl-v">relief</span><span class="pl-k">=</span>tk.<span class="pl-c1">GROOVE</span>)</td>
      </tr>
      <tr>
        <td id="L491" class="blob-num js-line-number" data-line-number="491"></td>
        <td id="LC491" class="blob-code blob-code-inner js-file-line">        optionmenu2.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">2</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W<span class="pl-k">+</span>tk.E<span class="pl-k">+</span>tk.S)</td>
      </tr>
      <tr>
        <td id="L492" class="blob-num js-line-number" data-line-number="492"></td>
        <td id="LC492" class="blob-code blob-code-inner js-file-line">        optionmenu2.config(<span class="pl-v">bg</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>gray97<span class="pl-pds">&quot;</span></span>, <span class="pl-v">relief</span><span class="pl-k">=</span>tk.<span class="pl-c1">GROOVE</span>)</td>
      </tr>
      <tr>
        <td id="L493" class="blob-num js-line-number" data-line-number="493"></td>
        <td id="LC493" class="blob-code blob-code-inner js-file-line">        button <span class="pl-k">=</span> tk.Button(<span class="pl-c1">self</span>.top_bivar, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">20</span>, <span class="pl-v">text</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>OK<span class="pl-pds">&quot;</span></span>, <span class="pl-v">command</span><span class="pl-k">=</span><span class="pl-k">lambda</span>: <span class="pl-c1">self</span>.plot_diagnostic(bivar_type), <span class="pl-v">bg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>gray97<span class="pl-pds">&#39;</span></span>, <span class="pl-v">relief</span><span class="pl-k">=</span>tk.<span class="pl-c1">GROOVE</span>)</td>
      </tr>
      <tr>
        <td id="L494" class="blob-num js-line-number" data-line-number="494"></td>
        <td id="LC494" class="blob-code blob-code-inner js-file-line">        button.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">3</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.S, <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">10</span>,<span class="pl-c1">10</span>))</td>
      </tr>
      <tr>
        <td id="L495" class="blob-num js-line-number" data-line-number="495"></td>
        <td id="LC495" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L496" class="blob-num js-line-number" data-line-number="496"></td>
        <td id="LC496" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Diagnostics buttons</span></td>
      </tr>
      <tr>
        <td id="L497" class="blob-num js-line-number" data-line-number="497"></td>
        <td id="LC497" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">diagn_buttons</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L498" class="blob-num js-line-number" data-line-number="498"></td>
        <td id="LC498" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:    <span class="pl-c1">self</span>.frame_diagn_but.destroy()</td>
      </tr>
      <tr>
        <td id="L499" class="blob-num js-line-number" data-line-number="499"></td>
        <td id="LC499" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span>: <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L500" class="blob-num js-line-number" data-line-number="500"></td>
        <td id="LC500" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.frame_diagn_but <span class="pl-k">=</span> tk.Frame(<span class="pl-c1">self</span>.frame_results)</td>
      </tr>
      <tr>
        <td id="L501" class="blob-num js-line-number" data-line-number="501"></td>
        <td id="LC501" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.frame_diagn_but.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">14</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.E<span class="pl-k">+</span>tk.W<span class="pl-k">+</span>tk.S, <span class="pl-v">padx</span><span class="pl-k">=</span><span class="pl-c1">10</span>, <span class="pl-v">pady</span><span class="pl-k">=</span><span class="pl-c1">10</span>)</td>
      </tr>
      <tr>
        <td id="L502" class="blob-num js-line-number" data-line-number="502"></td>
        <td id="LC502" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.frame_diagn_but.columnconfigure((<span class="pl-c1">0</span>,<span class="pl-c1">1</span>,<span class="pl-c1">2</span>), <span class="pl-v">weight</span><span class="pl-k">=</span><span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L503" class="blob-num js-line-number" data-line-number="503"></td>
        <td id="LC503" class="blob-code blob-code-inner js-file-line">        but_cle <span class="pl-k">=</span> tk.Button(<span class="pl-c1">self</span>.frame_diagn_but, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">10</span>, <span class="pl-v">text</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Clear<span class="pl-pds">&quot;</span></span>, <span class="pl-v">fg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>black<span class="pl-pds">&#39;</span></span>, <span class="pl-v">bg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>gray97<span class="pl-pds">&#39;</span></span>, <span class="pl-v">font</span><span class="pl-k">=</span>fontz[<span class="pl-s"><span class="pl-pds">&quot;</span>normal_small<span class="pl-pds">&quot;</span></span>],</td>
      </tr>
      <tr>
        <td id="L504" class="blob-num js-line-number" data-line-number="504"></td>
        <td id="LC504" class="blob-code blob-code-inner js-file-line">                            <span class="pl-v">command</span> <span class="pl-k">=</span> <span class="pl-k">lambda</span>: <span class="pl-c1">self</span>.clear(<span class="pl-v">menu</span><span class="pl-k">=</span><span class="pl-c1">True</span>), <span class="pl-v">relief</span><span class="pl-k">=</span>tk.<span class="pl-c1">GROOVE</span>)</td>
      </tr>
      <tr>
        <td id="L505" class="blob-num js-line-number" data-line-number="505"></td>
        <td id="LC505" class="blob-code blob-code-inner js-file-line">        but_cle.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">9</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">columnspan</span><span class="pl-k">=</span><span class="pl-c1">3</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.E<span class="pl-k">+</span>tk.S, <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">5</span>,<span class="pl-c1">0</span>))</td>
      </tr>
      <tr>
        <td id="L506" class="blob-num js-line-number" data-line-number="506"></td>
        <td id="LC506" class="blob-code blob-code-inner js-file-line">        but_mer <span class="pl-k">=</span> tk.Button(<span class="pl-c1">self</span>.frame_diagn_but, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">text</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Merge csv result files<span class="pl-pds">&quot;</span></span>, <span class="pl-v">fg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>black<span class="pl-pds">&#39;</span></span>, <span class="pl-v">bg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>gray97<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L507" class="blob-num js-line-number" data-line-number="507"></td>
        <td id="LC507" class="blob-code blob-code-inner js-file-line">                            <span class="pl-v">command</span> <span class="pl-k">=</span> <span class="pl-c1">self</span>.merge_csv_files, <span class="pl-v">font</span><span class="pl-k">=</span>fontz[<span class="pl-s"><span class="pl-pds">&quot;</span>normal_small<span class="pl-pds">&quot;</span></span>], <span class="pl-v">relief</span><span class="pl-k">=</span>tk.<span class="pl-c1">GROOVE</span>)</td>
      </tr>
      <tr>
        <td id="L508" class="blob-num js-line-number" data-line-number="508"></td>
        <td id="LC508" class="blob-code blob-code-inner js-file-line">        but_mer.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">columnspan</span><span class="pl-k">=</span><span class="pl-c1">3</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W<span class="pl-k">+</span>tk.E<span class="pl-k">+</span>tk.S, <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">5</span>,<span class="pl-c1">0</span>))</td>
      </tr>
      <tr>
        <td id="L509" class="blob-num js-line-number" data-line-number="509"></td>
        <td id="LC509" class="blob-code blob-code-inner js-file-line">        but_fit <span class="pl-k">=</span> tk.Button(<span class="pl-c1">self</span>.frame_diagn_but, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">text</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Draw data and fit<span class="pl-pds">&quot;</span></span>, <span class="pl-v">fg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>black<span class="pl-pds">&#39;</span></span>, <span class="pl-v">bg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>gray97<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L510" class="blob-num js-line-number" data-line-number="510"></td>
        <td id="LC510" class="blob-code blob-code-inner js-file-line">                            <span class="pl-v">command</span> <span class="pl-k">=</span> <span class="pl-c1">self</span>.plot_fit_now, <span class="pl-v">font</span><span class="pl-k">=</span>fontz[<span class="pl-s"><span class="pl-pds">&quot;</span>normal_small<span class="pl-pds">&quot;</span></span>], <span class="pl-v">relief</span><span class="pl-k">=</span>tk.<span class="pl-c1">GROOVE</span>)</td>
      </tr>
      <tr>
        <td id="L511" class="blob-num js-line-number" data-line-number="511"></td>
        <td id="LC511" class="blob-code blob-code-inner js-file-line">        but_fit.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W<span class="pl-k">+</span>tk.E<span class="pl-k">+</span>tk.S, <span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">5</span>,<span class="pl-c1">0</span>), <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">5</span>,<span class="pl-c1">0</span>))</td>
      </tr>
      <tr>
        <td id="L512" class="blob-num js-line-number" data-line-number="512"></td>
        <td id="LC512" class="blob-code blob-code-inner js-file-line">        but_dev <span class="pl-k">=</span> tk.Button(<span class="pl-c1">self</span>.frame_diagn_but, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">text</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Model deviance<span class="pl-pds">&quot;</span></span>, <span class="pl-v">fg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>black<span class="pl-pds">&#39;</span></span>, <span class="pl-v">bg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>gray97<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L513" class="blob-num js-line-number" data-line-number="513"></td>
        <td id="LC513" class="blob-code blob-code-inner js-file-line">                            <span class="pl-v">command</span> <span class="pl-k">=</span> <span class="pl-k">lambda</span>: <span class="pl-c1">self</span>.plot_diagnostic(<span class="pl-s"><span class="pl-pds">&quot;</span>deviance<span class="pl-pds">&quot;</span></span>), <span class="pl-v">font</span><span class="pl-k">=</span>fontz[<span class="pl-s"><span class="pl-pds">&quot;</span>normal_small<span class="pl-pds">&quot;</span></span>], <span class="pl-v">relief</span><span class="pl-k">=</span>tk.<span class="pl-c1">GROOVE</span>)</td>
      </tr>
      <tr>
        <td id="L514" class="blob-num js-line-number" data-line-number="514"></td>
        <td id="LC514" class="blob-code blob-code-inner js-file-line">        but_dev.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W<span class="pl-k">+</span>tk.E<span class="pl-k">+</span>tk.S, <span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">0</span>,<span class="pl-c1">0</span>), <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">5</span>,<span class="pl-c1">0</span>))</td>
      </tr>
      <tr>
        <td id="L515" class="blob-num js-line-number" data-line-number="515"></td>
        <td id="LC515" class="blob-code blob-code-inner js-file-line">        but_lik <span class="pl-k">=</span> tk.Button(<span class="pl-c1">self</span>.frame_diagn_but, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">text</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Log-likelihood<span class="pl-pds">&quot;</span></span>, <span class="pl-v">fg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>black<span class="pl-pds">&#39;</span></span>, <span class="pl-v">bg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>gray97<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L516" class="blob-num js-line-number" data-line-number="516"></td>
        <td id="LC516" class="blob-code blob-code-inner js-file-line">                            <span class="pl-v">command</span> <span class="pl-k">=</span> <span class="pl-k">lambda</span>: <span class="pl-c1">self</span>.plot_diagnostic(<span class="pl-s"><span class="pl-pds">&quot;</span>logp<span class="pl-pds">&quot;</span></span>), <span class="pl-v">font</span><span class="pl-k">=</span>fontz[<span class="pl-s"><span class="pl-pds">&quot;</span>normal_small<span class="pl-pds">&quot;</span></span>], <span class="pl-v">relief</span><span class="pl-k">=</span>tk.<span class="pl-c1">GROOVE</span>)</td>
      </tr>
      <tr>
        <td id="L517" class="blob-num js-line-number" data-line-number="517"></td>
        <td id="LC517" class="blob-code blob-code-inner js-file-line">        but_lik.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">2</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W<span class="pl-k">+</span>tk.E<span class="pl-k">+</span>tk.S, <span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">5</span>,<span class="pl-c1">0</span>), <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">5</span>,<span class="pl-c1">0</span>))</td>
      </tr>
      <tr>
        <td id="L518" class="blob-num js-line-number" data-line-number="518"></td>
        <td id="LC518" class="blob-code blob-code-inner js-file-line">        but_sum <span class="pl-k">=</span> tk.Button(<span class="pl-c1">self</span>.frame_diagn_but, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">text</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Summary and Gelman-Rubin convergence<span class="pl-pds">&quot;</span></span>, <span class="pl-v">fg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>black<span class="pl-pds">&#39;</span></span>, <span class="pl-v">bg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>gray97<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L519" class="blob-num js-line-number" data-line-number="519"></td>
        <td id="LC519" class="blob-code blob-code-inner js-file-line">                            <span class="pl-v">command</span> <span class="pl-k">=</span> <span class="pl-k">lambda</span>: <span class="pl-c1">self</span>.plot_diagnostic(<span class="pl-s"><span class="pl-pds">&quot;</span>summary<span class="pl-pds">&quot;</span></span>), <span class="pl-v">font</span><span class="pl-k">=</span>fontz[<span class="pl-s"><span class="pl-pds">&quot;</span>normal_small<span class="pl-pds">&quot;</span></span>], <span class="pl-v">relief</span><span class="pl-k">=</span>tk.<span class="pl-c1">GROOVE</span>)</td>
      </tr>
      <tr>
        <td id="L520" class="blob-num js-line-number" data-line-number="520"></td>
        <td id="LC520" class="blob-code blob-code-inner js-file-line">        but_sum.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">7</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">columnspan</span><span class="pl-k">=</span><span class="pl-c1">3</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W<span class="pl-k">+</span>tk.E<span class="pl-k">+</span>tk.S, <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">5</span>,<span class="pl-c1">0</span>))</td>
      </tr>
      <tr>
        <td id="L521" class="blob-num js-line-number" data-line-number="521"></td>
        <td id="LC521" class="blob-code blob-code-inner js-file-line">        but_hex <span class="pl-k">=</span> tk.Button(<span class="pl-c1">self</span>.frame_diagn_but, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">text</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Hex. binning<span class="pl-pds">&quot;</span></span>, <span class="pl-v">fg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>black<span class="pl-pds">&#39;</span></span>, <span class="pl-v">bg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>gray97<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L522" class="blob-num js-line-number" data-line-number="522"></td>
        <td id="LC522" class="blob-code blob-code-inner js-file-line">                            <span class="pl-v">command</span> <span class="pl-k">=</span> <span class="pl-k">lambda</span>: <span class="pl-c1">self</span>.popup_bivar(<span class="pl-s"><span class="pl-pds">&quot;</span>hexbin<span class="pl-pds">&quot;</span></span>), <span class="pl-v">font</span><span class="pl-k">=</span>fontz[<span class="pl-s"><span class="pl-pds">&quot;</span>normal_small<span class="pl-pds">&quot;</span></span>], <span class="pl-v">relief</span><span class="pl-k">=</span>tk.<span class="pl-c1">GROOVE</span>)</td>
      </tr>
      <tr>
        <td id="L523" class="blob-num js-line-number" data-line-number="523"></td>
        <td id="LC523" class="blob-code blob-code-inner js-file-line">        but_hex.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">2</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">columnspan</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W<span class="pl-k">+</span>tk.E<span class="pl-k">+</span>tk.S, <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">5</span>,<span class="pl-c1">0</span>))</td>
      </tr>
      <tr>
        <td id="L524" class="blob-num js-line-number" data-line-number="524"></td>
        <td id="LC524" class="blob-code blob-code-inner js-file-line">        but_kde <span class="pl-k">=</span> tk.Button(<span class="pl-c1">self</span>.frame_diagn_but, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">text</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Bivariate KDE<span class="pl-pds">&quot;</span></span>, <span class="pl-v">fg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>black<span class="pl-pds">&#39;</span></span>, <span class="pl-v">bg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>gray97<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L525" class="blob-num js-line-number" data-line-number="525"></td>
        <td id="LC525" class="blob-code blob-code-inner js-file-line">                            <span class="pl-v">command</span> <span class="pl-k">=</span> <span class="pl-k">lambda</span>: <span class="pl-c1">self</span>.popup_bivar(<span class="pl-s"><span class="pl-pds">&quot;</span>KDE<span class="pl-pds">&quot;</span></span>), <span class="pl-v">font</span><span class="pl-k">=</span>fontz[<span class="pl-s"><span class="pl-pds">&quot;</span>normal_small<span class="pl-pds">&quot;</span></span>], <span class="pl-v">relief</span><span class="pl-k">=</span>tk.<span class="pl-c1">GROOVE</span>)</td>
      </tr>
      <tr>
        <td id="L526" class="blob-num js-line-number" data-line-number="526"></td>
        <td id="LC526" class="blob-code blob-code-inner js-file-line">        but_kde.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">2</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">2</span>, <span class="pl-v">columnspan</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W<span class="pl-k">+</span>tk.E<span class="pl-k">+</span>tk.S, <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">5</span>,<span class="pl-c1">0</span>), <span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">5</span>,<span class="pl-c1">0</span>))</td>
      </tr>
      <tr>
        <td id="L527" class="blob-num js-line-number" data-line-number="527"></td>
        <td id="LC527" class="blob-code blob-code-inner js-file-line">        but_rld <span class="pl-k">=</span> tk.Button(<span class="pl-c1">self</span>.frame_diagn_but, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">text</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Raftery-Lewis diagnostic<span class="pl-pds">&quot;</span></span>, <span class="pl-v">fg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>black<span class="pl-pds">&#39;</span></span>, <span class="pl-v">bg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>gray97<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L528" class="blob-num js-line-number" data-line-number="528"></td>
        <td id="LC528" class="blob-code blob-code-inner js-file-line">                            <span class="pl-v">command</span> <span class="pl-k">=</span> <span class="pl-c1">self</span>.<span class="pl-c1">RLD_diagnostic</span>, <span class="pl-v">font</span><span class="pl-k">=</span>fontz[<span class="pl-s"><span class="pl-pds">&quot;</span>normal_small<span class="pl-pds">&quot;</span></span>], <span class="pl-v">relief</span><span class="pl-k">=</span>tk.<span class="pl-c1">GROOVE</span>)</td>
      </tr>
      <tr>
        <td id="L529" class="blob-num js-line-number" data-line-number="529"></td>
        <td id="LC529" class="blob-code blob-code-inner js-file-line">        but_rld.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">8</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">columnspan</span><span class="pl-k">=</span><span class="pl-c1">3</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W<span class="pl-k">+</span>tk.E<span class="pl-k">+</span>tk.S, <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">5</span>,<span class="pl-c1">5</span>))</td>
      </tr>
      <tr>
        <td id="L530" class="blob-num js-line-number" data-line-number="530"></td>
        <td id="LC530" class="blob-code blob-code-inner js-file-line">        but_tra <span class="pl-k">=</span> tk.Button(<span class="pl-c1">self</span>.frame_diagn_but, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">text</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Traces<span class="pl-pds">&quot;</span></span>, <span class="pl-v">fg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>black<span class="pl-pds">&#39;</span></span>, <span class="pl-v">bg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>gray97<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L531" class="blob-num js-line-number" data-line-number="531"></td>
        <td id="LC531" class="blob-code blob-code-inner js-file-line">                            <span class="pl-v">command</span> <span class="pl-k">=</span> <span class="pl-k">lambda</span>: <span class="pl-c1">self</span>.plot_diagnostic(<span class="pl-s"><span class="pl-pds">&quot;</span>traces<span class="pl-pds">&quot;</span></span>), <span class="pl-v">font</span><span class="pl-k">=</span>fontz[<span class="pl-s"><span class="pl-pds">&quot;</span>normal_small<span class="pl-pds">&quot;</span></span>], <span class="pl-v">relief</span><span class="pl-k">=</span>tk.<span class="pl-c1">GROOVE</span>)</td>
      </tr>
      <tr>
        <td id="L532" class="blob-num js-line-number" data-line-number="532"></td>
        <td id="LC532" class="blob-code blob-code-inner js-file-line">        but_tra.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">6</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W<span class="pl-k">+</span>tk.E<span class="pl-k">+</span>tk.S, <span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">0</span>,<span class="pl-c1">0</span>), <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">5</span>,<span class="pl-c1">0</span>))</td>
      </tr>
      <tr>
        <td id="L533" class="blob-num js-line-number" data-line-number="533"></td>
        <td id="LC533" class="blob-code blob-code-inner js-file-line">        but_his <span class="pl-k">=</span> tk.Button(<span class="pl-c1">self</span>.frame_diagn_but, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">text</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Histograms<span class="pl-pds">&quot;</span></span>, <span class="pl-v">fg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>black<span class="pl-pds">&#39;</span></span>, <span class="pl-v">bg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>gray97<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L534" class="blob-num js-line-number" data-line-number="534"></td>
        <td id="LC534" class="blob-code blob-code-inner js-file-line">                            <span class="pl-v">command</span> <span class="pl-k">=</span> <span class="pl-k">lambda</span>: <span class="pl-c1">self</span>.plot_diagnostic(<span class="pl-s"><span class="pl-pds">&quot;</span>histo<span class="pl-pds">&quot;</span></span>), <span class="pl-v">font</span><span class="pl-k">=</span>fontz[<span class="pl-s"><span class="pl-pds">&quot;</span>normal_small<span class="pl-pds">&quot;</span></span>], <span class="pl-v">relief</span><span class="pl-k">=</span>tk.<span class="pl-c1">GROOVE</span>)</td>
      </tr>
      <tr>
        <td id="L535" class="blob-num js-line-number" data-line-number="535"></td>
        <td id="LC535" class="blob-code blob-code-inner js-file-line">        but_his.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">6</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W<span class="pl-k">+</span>tk.E<span class="pl-k">+</span>tk.S, <span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">5</span>,<span class="pl-c1">0</span>), <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">5</span>,<span class="pl-c1">0</span>))</td>
      </tr>
      <tr>
        <td id="L536" class="blob-num js-line-number" data-line-number="536"></td>
        <td id="LC536" class="blob-code blob-code-inner js-file-line">        but_aut <span class="pl-k">=</span> tk.Button(<span class="pl-c1">self</span>.frame_diagn_but, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">text</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Autocorrelation<span class="pl-pds">&quot;</span></span>, <span class="pl-v">fg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>black<span class="pl-pds">&#39;</span></span>, <span class="pl-v">bg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>gray97<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L537" class="blob-num js-line-number" data-line-number="537"></td>
        <td id="LC537" class="blob-code blob-code-inner js-file-line">                            <span class="pl-v">command</span> <span class="pl-k">=</span> <span class="pl-k">lambda</span>: <span class="pl-c1">self</span>.plot_diagnostic(<span class="pl-s"><span class="pl-pds">&quot;</span>autocorr<span class="pl-pds">&quot;</span></span>), <span class="pl-v">font</span><span class="pl-k">=</span>fontz[<span class="pl-s"><span class="pl-pds">&quot;</span>normal_small<span class="pl-pds">&quot;</span></span>], <span class="pl-v">relief</span><span class="pl-k">=</span>tk.<span class="pl-c1">GROOVE</span>)</td>
      </tr>
      <tr>
        <td id="L538" class="blob-num js-line-number" data-line-number="538"></td>
        <td id="LC538" class="blob-code blob-code-inner js-file-line">        but_aut.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">6</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">2</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W<span class="pl-k">+</span>tk.E<span class="pl-k">+</span>tk.S, <span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">5</span>,<span class="pl-c1">0</span>), <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">5</span>,<span class="pl-c1">0</span>))</td>
      </tr>
      <tr>
        <td id="L539" class="blob-num js-line-number" data-line-number="539"></td>
        <td id="LC539" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.model.get() <span class="pl-k">in</span> [<span class="pl-s"><span class="pl-pds">&quot;</span>PDecomp<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>CCD<span class="pl-pds">&quot;</span></span>]:</td>
      </tr>
      <tr>
        <td id="L540" class="blob-num js-line-number" data-line-number="540"></td>
        <td id="LC540" class="blob-code blob-code-inner js-file-line">            but_rtd <span class="pl-k">=</span> tk.Button(<span class="pl-c1">self</span>.frame_diagn_but, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">text</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Relaxation time distribution<span class="pl-pds">&quot;</span></span>, <span class="pl-v">fg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>black<span class="pl-pds">&#39;</span></span>, <span class="pl-v">bg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>gray97<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L541" class="blob-num js-line-number" data-line-number="541"></td>
        <td id="LC541" class="blob-code blob-code-inner js-file-line">                                <span class="pl-v">command</span> <span class="pl-k">=</span> <span class="pl-c1">self</span>.plot_rtd_now, <span class="pl-v">font</span><span class="pl-k">=</span>fontz[<span class="pl-s"><span class="pl-pds">&quot;</span>normal_small<span class="pl-pds">&quot;</span></span>], <span class="pl-v">relief</span><span class="pl-k">=</span>tk.<span class="pl-c1">GROOVE</span>)</td>
      </tr>
      <tr>
        <td id="L542" class="blob-num js-line-number" data-line-number="542"></td>
        <td id="LC542" class="blob-code blob-code-inner js-file-line">            but_rtd.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">5</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">columnspan</span><span class="pl-k">=</span><span class="pl-c1">3</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W<span class="pl-k">+</span>tk.E<span class="pl-k">+</span>tk.S, <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">5</span>,<span class="pl-c1">0</span>))</td>
      </tr>
      <tr>
        <td id="L543" class="blob-num js-line-number" data-line-number="543"></td>
        <td id="LC543" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L544" class="blob-num js-line-number" data-line-number="544"></td>
        <td id="LC544" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">write_output_path</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L545" class="blob-num js-line-number" data-line-number="545"></td>
        <td id="LC545" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:    <span class="pl-c1">self</span>.frame_saved_in.destroy()</td>
      </tr>
      <tr>
        <td id="L546" class="blob-num js-line-number" data-line-number="546"></td>
        <td id="LC546" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span>: <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L547" class="blob-num js-line-number" data-line-number="547"></td>
        <td id="LC547" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.frame_saved_in <span class="pl-k">=</span> tk.Frame(<span class="pl-c1">self</span>.frame_results)</td>
      </tr>
      <tr>
        <td id="L548" class="blob-num js-line-number" data-line-number="548"></td>
        <td id="LC548" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.frame_saved_in.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">8</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.E<span class="pl-k">+</span>tk.W, <span class="pl-v">padx</span><span class="pl-k">=</span><span class="pl-c1">10</span>, <span class="pl-v">pady</span><span class="pl-k">=</span><span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L549" class="blob-num js-line-number" data-line-number="549"></td>
        <td id="LC549" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.frame_saved_in.columnconfigure(<span class="pl-c1">0</span>, <span class="pl-v">weight</span><span class="pl-k">=</span><span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L550" class="blob-num js-line-number" data-line-number="550"></td>
        <td id="LC550" class="blob-code blob-code-inner js-file-line">        label_done <span class="pl-k">=</span> tk.Label(<span class="pl-c1">self</span>.frame_saved_in, <span class="pl-v">text</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Results saved in:<span class="pl-pds">&quot;&quot;&quot;</span></span>, <span class="pl-v">anchor</span><span class="pl-k">=</span>tk.W)</td>
      </tr>
      <tr>
        <td id="L551" class="blob-num js-line-number" data-line-number="551"></td>
        <td id="LC551" class="blob-code blob-code-inner js-file-line">        label_done.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">columnspan</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W<span class="pl-k">+</span>tk.E)</td>
      </tr>
      <tr>
        <td id="L552" class="blob-num js-line-number" data-line-number="552"></td>
        <td id="LC552" class="blob-code blob-code-inner js-file-line">        text_path <span class="pl-k">=</span> tk.Text(<span class="pl-c1">self</span>.frame_saved_in, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">3</span>, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">35</span>, <span class="pl-v">font</span><span class="pl-k">=</span>fontz[<span class="pl-s"><span class="pl-pds">&quot;</span>normal_small<span class="pl-pds">&quot;</span></span>])</td>
      </tr>
      <tr>
        <td id="L553" class="blob-num js-line-number" data-line-number="553"></td>
        <td id="LC553" class="blob-code blob-code-inner js-file-line">        text_path.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">columnspan</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W<span class="pl-k">+</span>tk.E, <span class="pl-v">padx</span><span class="pl-k">=</span><span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L554" class="blob-num js-line-number" data-line-number="554"></td>
        <td id="LC554" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.run_options[<span class="pl-s"><span class="pl-pds">&quot;</span>Save CSV results<span class="pl-pds">&quot;</span></span>].get():         </td>
      </tr>
      <tr>
        <td id="L555" class="blob-num js-line-number" data-line-number="555"></td>
        <td id="LC555" class="blob-code blob-code-inner js-file-line">            text_path.insert(<span class="pl-s"><span class="pl-pds">&quot;</span>1.0<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span>(<span class="pl-c1">self</span>.working_path))</td>
      </tr>
      <tr>
        <td id="L556" class="blob-num js-line-number" data-line-number="556"></td>
        <td id="LC556" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L557" class="blob-num js-line-number" data-line-number="557"></td>
        <td id="LC557" class="blob-code blob-code-inner js-file-line">            text_path.insert(<span class="pl-s"><span class="pl-pds">&quot;</span>1.0<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>RESULTS NOT SAVED. CSV SAVE OPTION IS UNCHECKED.<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L558" class="blob-num js-line-number" data-line-number="558"></td>
        <td id="LC558" class="blob-code blob-code-inner js-file-line">            </td>
      </tr>
      <tr>
        <td id="L559" class="blob-num js-line-number" data-line-number="559"></td>
        <td id="LC559" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">update_results</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L560" class="blob-num js-line-number" data-line-number="560"></td>
        <td id="LC560" class="blob-code blob-code-inner js-file-line">        pm <span class="pl-k">=</span> <span class="pl-c1">self</span>.all_results[<span class="pl-c1">self</span>.var_review.get()][<span class="pl-s"><span class="pl-pds">&quot;</span>pm<span class="pl-pds">&quot;</span></span>]</td>
      </tr>
      <tr>
        <td id="L561" class="blob-num js-line-number" data-line-number="561"></td>
        <td id="LC561" class="blob-code blob-code-inner js-file-line">        model <span class="pl-k">=</span> <span class="pl-c1">self</span>.model.get()</td>
      </tr>
      <tr>
        <td id="L562" class="blob-num js-line-number" data-line-number="562"></td>
        <td id="LC562" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:    <span class="pl-c1">self</span>.frame_optimal.destroy()</td>
      </tr>
      <tr>
        <td id="L563" class="blob-num js-line-number" data-line-number="563"></td>
        <td id="LC563" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span>: <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L564" class="blob-num js-line-number" data-line-number="564"></td>
        <td id="LC564" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.frame_optimal <span class="pl-k">=</span> tk.Frame(<span class="pl-c1">self</span>.frame_results)</td>
      </tr>
      <tr>
        <td id="L565" class="blob-num js-line-number" data-line-number="565"></td>
        <td id="LC565" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.frame_optimal.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">2</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.E<span class="pl-k">+</span>tk.W, <span class="pl-v">padx</span><span class="pl-k">=</span><span class="pl-c1">10</span>, <span class="pl-v">pady</span><span class="pl-k">=</span><span class="pl-c1">10</span>)</td>
      </tr>
      <tr>
        <td id="L566" class="blob-num js-line-number" data-line-number="566"></td>
        <td id="LC566" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.frame_optimal.columnconfigure(<span class="pl-c1">0</span>, <span class="pl-v">weight</span><span class="pl-k">=</span><span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L567" class="blob-num js-line-number" data-line-number="567"></td>
        <td id="LC567" class="blob-code blob-code-inner js-file-line">        keys <span class="pl-k">=</span> <span class="pl-c1">sorted</span>([x <span class="pl-k">for</span> x <span class="pl-k">in</span> <span class="pl-c1">list</span>(pm.keys()) <span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&quot;</span>_std<span class="pl-pds">&quot;</span></span> <span class="pl-k">not</span> <span class="pl-k">in</span> x])</td>
      </tr>
      <tr>
        <td id="L568" class="blob-num js-line-number" data-line-number="568"></td>
        <td id="LC568" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L569" class="blob-num js-line-number" data-line-number="569"></td>
        <td id="LC569" class="blob-code blob-code-inner js-file-line">            keys.remove(<span class="pl-s"><span class="pl-pds">&quot;</span>m_i<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L570" class="blob-num js-line-number" data-line-number="570"></td>
        <td id="LC570" class="blob-code blob-code-inner js-file-line">            keys.remove(<span class="pl-s"><span class="pl-pds">&quot;</span>tau_i<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L571" class="blob-num js-line-number" data-line-number="571"></td>
        <td id="LC571" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L572" class="blob-num js-line-number" data-line-number="572"></td>
        <td id="LC572" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L573" class="blob-num js-line-number" data-line-number="573"></td>
        <td id="LC573" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L574" class="blob-num js-line-number" data-line-number="574"></td>
        <td id="LC574" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> model <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>PDecomp<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L575" class="blob-num js-line-number" data-line-number="575"></td>
        <td id="LC575" class="blob-code blob-code-inner js-file-line">            adj <span class="pl-k">=</span> <span class="pl-k">-</span><span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L576" class="blob-num js-line-number" data-line-number="576"></td>
        <td id="LC576" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L577" class="blob-num js-line-number" data-line-number="577"></td>
        <td id="LC577" class="blob-code blob-code-inner js-file-line">            adj <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L578" class="blob-num js-line-number" data-line-number="578"></td>
        <td id="LC578" class="blob-code blob-code-inner js-file-line">        noise_where <span class="pl-k">=</span> [i <span class="pl-k">for</span> i, k <span class="pl-k">in</span> <span class="pl-c1">enumerate</span>(keys) <span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&quot;</span>noise<span class="pl-pds">&quot;</span></span> <span class="pl-k">in</span> k]</td>
      </tr>
      <tr>
        <td id="L579" class="blob-num js-line-number" data-line-number="579"></td>
        <td id="LC579" class="blob-code blob-code-inner js-file-line">        values <span class="pl-k">=</span> flatten([pm[k] <span class="pl-k">for</span> k <span class="pl-k">in</span> <span class="pl-c1">sorted</span>(keys)])</td>
      </tr>
      <tr>
        <td id="L580" class="blob-num js-line-number" data-line-number="580"></td>
        <td id="LC580" class="blob-code blob-code-inner js-file-line">        errors <span class="pl-k">=</span> flatten([pm[k<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span>_std<span class="pl-pds">&quot;</span></span>] <span class="pl-k">for</span> k <span class="pl-k">in</span> <span class="pl-c1">sorted</span>(keys)])</td>
      </tr>
      <tr>
        <td id="L581" class="blob-num js-line-number" data-line-number="581"></td>
        <td id="LC581" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> (i, k) <span class="pl-k">in</span> <span class="pl-c1">enumerate</span>(keys):</td>
      </tr>
      <tr>
        <td id="L582" class="blob-num js-line-number" data-line-number="582"></td>
        <td id="LC582" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">len</span>(pm[k].shape) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L583" class="blob-num js-line-number" data-line-number="583"></td>
        <td id="LC583" class="blob-code blob-code-inner js-file-line">                keys[i] <span class="pl-k">=</span> [keys[i]<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">%d</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>n <span class="pl-k">for</span> n <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-c1">1</span><span class="pl-k">+</span>adj,pm[k].shape[<span class="pl-c1">0</span>]<span class="pl-k">+</span><span class="pl-c1">1</span><span class="pl-k">+</span>adj)]</td>
      </tr>
      <tr>
        <td id="L584" class="blob-num js-line-number" data-line-number="584"></td>
        <td id="LC584" class="blob-code blob-code-inner js-file-line">        keys <span class="pl-k">=</span> <span class="pl-c1">list</span>(flatten(keys))</td>
      </tr>
      <tr>
        <td id="L585" class="blob-num js-line-number" data-line-number="585"></td>
        <td id="LC585" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.list_of_parameters <span class="pl-k">=</span> keys</td>
      </tr>
      <tr>
        <td id="L586" class="blob-num js-line-number" data-line-number="586"></td>
        <td id="LC586" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>        for c, k in enumerate(self.list_of_parameters):</span></td>
      </tr>
      <tr>
        <td id="L587" class="blob-num js-line-number" data-line-number="587"></td>
        <td id="LC587" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>            if &quot;tau&quot; in k:</span></td>
      </tr>
      <tr>
        <td id="L588" class="blob-num js-line-number" data-line-number="588"></td>
        <td id="LC588" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>                self.list_of_parameters[c] = &quot;log_&quot;+k</span></td>
      </tr>
      <tr>
        <td id="L589" class="blob-num js-line-number" data-line-number="589"></td>
        <td id="LC589" class="blob-code blob-code-inner js-file-line">        label_res <span class="pl-k">=</span> tk.Label(<span class="pl-c1">self</span>.frame_optimal, <span class="pl-v">text</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Optimal parameters:<span class="pl-pds">&quot;&quot;&quot;</span></span>, <span class="pl-v">anchor</span><span class="pl-k">=</span>tk.W)</td>
      </tr>
      <tr>
        <td id="L590" class="blob-num js-line-number" data-line-number="590"></td>
        <td id="LC590" class="blob-code blob-code-inner js-file-line">        label_res.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W<span class="pl-k">+</span>tk.E<span class="pl-k">+</span>tk.N)</td>
      </tr>
      <tr>
        <td id="L591" class="blob-num js-line-number" data-line-number="591"></td>
        <td id="LC591" class="blob-code blob-code-inner js-file-line">        text_res <span class="pl-k">=</span> tk.Text(<span class="pl-c1">self</span>.frame_optimal, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">len</span>(values), <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">40</span>, <span class="pl-v">font</span><span class="pl-k">=</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>Courier new<span class="pl-pds">&quot;</span></span>, fontsize<span class="pl-k">+</span>res_size, <span class="pl-s"><span class="pl-pds">&quot;</span>bold<span class="pl-pds">&quot;</span></span>))</td>
      </tr>
      <tr>
        <td id="L592" class="blob-num js-line-number" data-line-number="592"></td>
        <td id="LC592" class="blob-code blob-code-inner js-file-line">        text_res.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W<span class="pl-k">+</span>tk.E<span class="pl-k">+</span>tk.N)</td>
      </tr>
      <tr>
        <td id="L593" class="blob-num js-line-number" data-line-number="593"></td>
        <td id="LC593" class="blob-code blob-code-inner js-file-line">        items <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">{<span class="pl-k">:&lt;13</span>}</span><span class="pl-pds">&quot;</span></span>.format(x<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span>:<span class="pl-pds">&quot;</span></span>) <span class="pl-k">for</span> x <span class="pl-k">in</span> keys]</td>
      </tr>
      <tr>
        <td id="L594" class="blob-num js-line-number" data-line-number="594"></td>
        <td id="LC594" class="blob-code blob-code-inner js-file-line">        items2 <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&quot;</span> <span class="pl-c1">%.3e</span> <span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span>x <span class="pl-k">for</span> x <span class="pl-k">in</span> values]</td>
      </tr>
      <tr>
        <td id="L595" class="blob-num js-line-number" data-line-number="595"></td>
        <td id="LC595" class="blob-code blob-code-inner js-file-line">        items3 <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&quot;</span>+/- <span class="pl-c1">%.0e</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span>x <span class="pl-k">for</span> x <span class="pl-k">in</span> errors]</td>
      </tr>
      <tr>
        <td id="L596" class="blob-num js-line-number" data-line-number="596"></td>
        <td id="LC596" class="blob-code blob-code-inner js-file-line">        items4 <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&quot;</span> (<span class="pl-c1">%.2f%%</span>)<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span>(<span class="pl-c1">abs</span>(<span class="pl-c1">100</span><span class="pl-k">*</span>e<span class="pl-k">/</span>v)) <span class="pl-k">for</span> v,e <span class="pl-k">in</span> <span class="pl-c1">zip</span>(values,errors)]</td>
      </tr>
      <tr>
        <td id="L597" class="blob-num js-line-number" data-line-number="597"></td>
        <td id="LC597" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L598" class="blob-num js-line-number" data-line-number="598"></td>
        <td id="LC598" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> n <span class="pl-k">in</span> noise_where:</td>
      </tr>
      <tr>
        <td id="L599" class="blob-num js-line-number" data-line-number="599"></td>
        <td id="LC599" class="blob-code blob-code-inner js-file-line">            items4[n]<span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span> (-.--%)<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L600" class="blob-num js-line-number" data-line-number="600"></td>
        <td id="LC600" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L601" class="blob-num js-line-number" data-line-number="601"></td>
        <td id="LC601" class="blob-code blob-code-inner js-file-line">        all_items <span class="pl-k">=</span> [a_<span class="pl-k">+</span>b_<span class="pl-k">+</span>c_<span class="pl-k">+</span>d_ <span class="pl-k">for</span> a_,b_,c_,d_ <span class="pl-k">in</span> <span class="pl-c1">zip</span>(items,items2,items3,items4)]</td>
      </tr>
      <tr>
        <td id="L602" class="blob-num js-line-number" data-line-number="602"></td>
        <td id="LC602" class="blob-code blob-code-inner js-file-line">        items <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>.join(all_items)</td>
      </tr>
      <tr>
        <td id="L603" class="blob-num js-line-number" data-line-number="603"></td>
        <td id="LC603" class="blob-code blob-code-inner js-file-line">        text_res.insert(<span class="pl-s"><span class="pl-pds">&quot;</span>1.0<span class="pl-pds">&quot;</span></span>, items)</td>
      </tr>
      <tr>
        <td id="L604" class="blob-num js-line-number" data-line-number="604"></td>
        <td id="LC604" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L605" class="blob-num js-line-number" data-line-number="605"></td>
        <td id="LC605" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>==============================================================================</span></td>
      </tr>
      <tr>
        <td id="L606" class="blob-num js-line-number" data-line-number="606"></td>
        <td id="LC606" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> MCMC parameters</span></td>
      </tr>
      <tr>
        <td id="L607" class="blob-num js-line-number" data-line-number="607"></td>
        <td id="LC607" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>==============================================================================</span></td>
      </tr>
      <tr>
        <td id="L608" class="blob-num js-line-number" data-line-number="608"></td>
        <td id="LC608" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">mcmc_parameters</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L609" class="blob-num js-line-number" data-line-number="609"></td>
        <td id="LC609" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> McMC parameters</span></td>
      </tr>
      <tr>
        <td id="L610" class="blob-num js-line-number" data-line-number="610"></td>
        <td id="LC610" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.adaptive <span class="pl-k">=</span> tk.BooleanVar()</td>
      </tr>
      <tr>
        <td id="L611" class="blob-num js-line-number" data-line-number="611"></td>
        <td id="LC611" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.adaptive_text <span class="pl-k">=</span> tk.StringVar()</td>
      </tr>
      <tr>
        <td id="L612" class="blob-num js-line-number" data-line-number="612"></td>
        <td id="LC612" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">def</span> <span class="pl-en">yesno</span>():</td>
      </tr>
      <tr>
        <td id="L613" class="blob-num js-line-number" data-line-number="613"></td>
        <td id="LC613" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">self</span>.adaptive.get():</td>
      </tr>
      <tr>
        <td id="L614" class="blob-num js-line-number" data-line-number="614"></td>
        <td id="LC614" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.adaptive_text.set(<span class="pl-s"><span class="pl-pds">&quot;</span>AM<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L615" class="blob-num js-line-number" data-line-number="615"></td>
        <td id="LC615" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">for</span> i, (k, v) <span class="pl-k">in</span> <span class="pl-c1">enumerate</span>(<span class="pl-c1">self</span>.mcmc_vars.items()):</td>
      </tr>
      <tr>
        <td id="L616" class="blob-num js-line-number" data-line-number="616"></td>
        <td id="LC616" class="blob-code blob-code-inner js-file-line">                    v[<span class="pl-c1">0</span>].set(<span class="pl-c1">self</span>.root_ini[k])</td>
      </tr>
      <tr>
        <td id="L617" class="blob-num js-line-number" data-line-number="617"></td>
        <td id="LC617" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">if</span> k <span class="pl-k">in</span> [<span class="pl-s"><span class="pl-pds">&quot;</span>Tuning interval<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>Proposal scale<span class="pl-pds">&quot;</span></span>]:</td>
      </tr>
      <tr>
        <td id="L618" class="blob-num js-line-number" data-line-number="618"></td>
        <td id="LC618" class="blob-code blob-code-inner js-file-line">                        tk.Entry(<span class="pl-c1">self</span>.frame_mcmc ,<span class="pl-v">textvariable</span><span class="pl-k">=</span>v[<span class="pl-c1">0</span>],<span class="pl-v">fg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>grey<span class="pl-pds">&quot;</span></span>, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">12</span>).grid(<span class="pl-v">row</span><span class="pl-k">=</span>i<span class="pl-k">+</span><span class="pl-c1">1</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.E,<span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">0</span>,<span class="pl-c1">10</span>))</td>
      </tr>
      <tr>
        <td id="L619" class="blob-num js-line-number" data-line-number="619"></td>
        <td id="LC619" class="blob-code blob-code-inner js-file-line">                        tk.Label(<span class="pl-c1">self</span>.frame_mcmc, <span class="pl-v">text</span><span class="pl-k">=</span>k, <span class="pl-v">justify</span> <span class="pl-k">=</span> tk.<span class="pl-c1">LEFT</span>, <span class="pl-v">fg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>grey<span class="pl-pds">&quot;</span></span>).grid(<span class="pl-v">row</span><span class="pl-k">=</span>i<span class="pl-k">+</span><span class="pl-c1">1</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W, <span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">10</span>,<span class="pl-c1">0</span>))</td>
      </tr>
      <tr>
        <td id="L620" class="blob-num js-line-number" data-line-number="620"></td>
        <td id="LC620" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L621" class="blob-num js-line-number" data-line-number="621"></td>
        <td id="LC621" class="blob-code blob-code-inner js-file-line">                        tk.Entry(<span class="pl-c1">self</span>.frame_mcmc ,<span class="pl-v">textvariable</span><span class="pl-k">=</span>v[<span class="pl-c1">0</span>], <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">12</span>).grid(<span class="pl-v">row</span><span class="pl-k">=</span>i<span class="pl-k">+</span><span class="pl-c1">1</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.E,<span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">0</span>,<span class="pl-c1">10</span>))</td>
      </tr>
      <tr>
        <td id="L622" class="blob-num js-line-number" data-line-number="622"></td>
        <td id="LC622" class="blob-code blob-code-inner js-file-line">                        tk.Label(<span class="pl-c1">self</span>.frame_mcmc, <span class="pl-v">text</span><span class="pl-k">=</span>k, <span class="pl-v">justify</span> <span class="pl-k">=</span> tk.<span class="pl-c1">LEFT</span>).grid(<span class="pl-v">row</span><span class="pl-k">=</span>i<span class="pl-k">+</span><span class="pl-c1">1</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W, <span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">10</span>,<span class="pl-c1">0</span>))</td>
      </tr>
      <tr>
        <td id="L623" class="blob-num js-line-number" data-line-number="623"></td>
        <td id="LC623" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L624" class="blob-num js-line-number" data-line-number="624"></td>
        <td id="LC624" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.adaptive_text.set(<span class="pl-s"><span class="pl-pds">&quot;</span>MH<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L625" class="blob-num js-line-number" data-line-number="625"></td>
        <td id="LC625" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">for</span> i, (k, v) <span class="pl-k">in</span> <span class="pl-c1">enumerate</span>(<span class="pl-c1">self</span>.mcmc_vars.items()):</td>
      </tr>
      <tr>
        <td id="L626" class="blob-num js-line-number" data-line-number="626"></td>
        <td id="LC626" class="blob-code blob-code-inner js-file-line">                    v[<span class="pl-c1">0</span>].set(<span class="pl-c1">self</span>.root_ini[k])</td>
      </tr>
      <tr>
        <td id="L627" class="blob-num js-line-number" data-line-number="627"></td>
        <td id="LC627" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">if</span> k <span class="pl-k">in</span> [<span class="pl-s"><span class="pl-pds">&quot;</span>Covariance interval<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>Covariance delay<span class="pl-pds">&quot;</span></span>]:</td>
      </tr>
      <tr>
        <td id="L628" class="blob-num js-line-number" data-line-number="628"></td>
        <td id="LC628" class="blob-code blob-code-inner js-file-line">                        tk.Entry(<span class="pl-c1">self</span>.frame_mcmc ,<span class="pl-v">textvariable</span><span class="pl-k">=</span>v[<span class="pl-c1">0</span>],<span class="pl-v">fg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>grey<span class="pl-pds">&quot;</span></span>, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">12</span>).grid(<span class="pl-v">row</span><span class="pl-k">=</span>i<span class="pl-k">+</span><span class="pl-c1">1</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.E,<span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">0</span>,<span class="pl-c1">10</span>))</td>
      </tr>
      <tr>
        <td id="L629" class="blob-num js-line-number" data-line-number="629"></td>
        <td id="LC629" class="blob-code blob-code-inner js-file-line">                        tk.Label(<span class="pl-c1">self</span>.frame_mcmc, <span class="pl-v">text</span><span class="pl-k">=</span>k, <span class="pl-v">justify</span> <span class="pl-k">=</span> tk.<span class="pl-c1">LEFT</span>, <span class="pl-v">fg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>grey<span class="pl-pds">&quot;</span></span>).grid(<span class="pl-v">row</span><span class="pl-k">=</span>i<span class="pl-k">+</span><span class="pl-c1">1</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W, <span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">10</span>,<span class="pl-c1">0</span>))</td>
      </tr>
      <tr>
        <td id="L630" class="blob-num js-line-number" data-line-number="630"></td>
        <td id="LC630" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L631" class="blob-num js-line-number" data-line-number="631"></td>
        <td id="LC631" class="blob-code blob-code-inner js-file-line">                        tk.Entry(<span class="pl-c1">self</span>.frame_mcmc ,<span class="pl-v">textvariable</span><span class="pl-k">=</span>v[<span class="pl-c1">0</span>], <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">12</span>).grid(<span class="pl-v">row</span><span class="pl-k">=</span>i<span class="pl-k">+</span><span class="pl-c1">1</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.E,<span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">0</span>,<span class="pl-c1">10</span>))</td>
      </tr>
      <tr>
        <td id="L632" class="blob-num js-line-number" data-line-number="632"></td>
        <td id="LC632" class="blob-code blob-code-inner js-file-line">                        tk.Label(<span class="pl-c1">self</span>.frame_mcmc, <span class="pl-v">text</span><span class="pl-k">=</span>k, <span class="pl-v">justify</span> <span class="pl-k">=</span> tk.<span class="pl-c1">LEFT</span>).grid(<span class="pl-v">row</span><span class="pl-k">=</span>i<span class="pl-k">+</span><span class="pl-c1">1</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W, <span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">10</span>,<span class="pl-c1">0</span>))</td>
      </tr>
      <tr>
        <td id="L633" class="blob-num js-line-number" data-line-number="633"></td>
        <td id="LC633" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L634" class="blob-num js-line-number" data-line-number="634"></td>
        <td id="LC634" class="blob-code blob-code-inner js-file-line">        tk.Label(<span class="pl-c1">self</span>.frame_mcmc, <span class="pl-v">text</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Use Adaptive Metropolis:<span class="pl-pds">&quot;</span></span>, <span class="pl-v">justify</span> <span class="pl-k">=</span> tk.<span class="pl-c1">LEFT</span>).grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W, <span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">10</span>,<span class="pl-c1">0</span>))</td>
      </tr>
      <tr>
        <td id="L635" class="blob-num js-line-number" data-line-number="635"></td>
        <td id="LC635" class="blob-code blob-code-inner js-file-line">        tk.Checkbutton(<span class="pl-c1">self</span>.frame_mcmc , <span class="pl-v">variable</span><span class="pl-k">=</span><span class="pl-c1">self</span>.adaptive, <span class="pl-v">textvariable</span><span class="pl-k">=</span><span class="pl-c1">self</span>.adaptive_text, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">12</span>, <span class="pl-v">command</span><span class="pl-k">=</span>yesno).grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.E,<span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">0</span>,<span class="pl-c1">10</span>))</td>
      </tr>
      <tr>
        <td id="L636" class="blob-num js-line-number" data-line-number="636"></td>
        <td id="LC636" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.adaptive.set(<span class="pl-c1">self</span>.root_ini[<span class="pl-s"><span class="pl-pds">&quot;</span>Adaptive Metropolis<span class="pl-pds">&quot;</span></span>])</td>
      </tr>
      <tr>
        <td id="L637" class="blob-num js-line-number" data-line-number="637"></td>
        <td id="LC637" class="blob-code blob-code-inner js-file-line">        yesno()</td>
      </tr>
      <tr>
        <td id="L638" class="blob-num js-line-number" data-line-number="638"></td>
        <td id="LC638" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L639" class="blob-num js-line-number" data-line-number="639"></td>
        <td id="LC639" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>==============================================================================</span></td>
      </tr>
      <tr>
        <td id="L640" class="blob-num js-line-number" data-line-number="640"></td>
        <td id="LC640" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> SIP model</span></td>
      </tr>
      <tr>
        <td id="L641" class="blob-num js-line-number" data-line-number="641"></td>
        <td id="LC641" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>==============================================================================</span></td>
      </tr>
      <tr>
        <td id="L642" class="blob-num js-line-number" data-line-number="642"></td>
        <td id="LC642" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">model_choice</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L643" class="blob-num js-line-number" data-line-number="643"></td>
        <td id="LC643" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> Available models</span></td>
      </tr>
      <tr>
        <td id="L644" class="blob-num js-line-number" data-line-number="644"></td>
        <td id="LC644" class="blob-code blob-code-inner js-file-line">        models <span class="pl-k">=</span> [(<span class="pl-s"><span class="pl-pds">&quot;</span>Pelton Cole-Cole<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>ColeCole<span class="pl-pds">&quot;</span></span>),</td>
      </tr>
      <tr>
        <td id="L645" class="blob-num js-line-number" data-line-number="645"></td>
        <td id="LC645" class="blob-code blob-code-inner js-file-line">                  (<span class="pl-s"><span class="pl-pds">&quot;</span>Dias model<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>Dias<span class="pl-pds">&quot;</span></span>),</td>
      </tr>
      <tr>
        <td id="L646" class="blob-num js-line-number" data-line-number="646"></td>
        <td id="LC646" class="blob-code blob-code-inner js-file-line">                  (<span class="pl-s"><span class="pl-pds">&quot;</span>Polynomial decomposition<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>PDecomp<span class="pl-pds">&quot;</span></span>),</td>
      </tr>
      <tr>
        <td id="L647" class="blob-num js-line-number" data-line-number="647"></td>
        <td id="LC647" class="blob-code blob-code-inner js-file-line">                  (<span class="pl-s"><span class="pl-pds">&quot;</span>Stochastic CCDtools<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>CCD<span class="pl-pds">&quot;</span></span>),</td>
      </tr>
      <tr>
        <td id="L648" class="blob-num js-line-number" data-line-number="648"></td>
        <td id="LC648" class="blob-code blob-code-inner js-file-line">                  ]</td>
      </tr>
      <tr>
        <td id="L649" class="blob-num js-line-number" data-line-number="649"></td>
        <td id="LC649" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.lamb_da, <span class="pl-c1">self</span>.modes_n, <span class="pl-c1">self</span>.poly_n, <span class="pl-c1">self</span>.c_exp <span class="pl-k">=</span> tk.DoubleVar(), tk.IntVar(), tk.IntVar(), tk.DoubleVar()</td>
      </tr>
      <tr>
        <td id="L650" class="blob-num js-line-number" data-line-number="650"></td>
        <td id="LC650" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.modes_n.set(<span class="pl-c1">self</span>.root_ini[<span class="pl-s"><span class="pl-pds">&quot;</span>Nb modes<span class="pl-pds">&quot;</span></span>]), <span class="pl-c1">self</span>.poly_n.set(<span class="pl-c1">self</span>.root_ini[<span class="pl-s"><span class="pl-pds">&quot;</span>Polyn order<span class="pl-pds">&quot;</span></span>]), <span class="pl-c1">self</span>.c_exp.set(<span class="pl-c1">self</span>.root_ini[<span class="pl-s"><span class="pl-pds">&quot;</span>Freq dep<span class="pl-pds">&quot;</span></span>])</td>
      </tr>
      <tr>
        <td id="L651" class="blob-num js-line-number" data-line-number="651"></td>
        <td id="LC651" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.lamb_da.set(<span class="pl-c1">self</span>.root_ini[<span class="pl-s"><span class="pl-pds">&quot;</span>Lambda<span class="pl-pds">&quot;</span></span>])</td>
      </tr>
      <tr>
        <td id="L652" class="blob-num js-line-number" data-line-number="652"></td>
        <td id="LC652" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L653" class="blob-num js-line-number" data-line-number="653"></td>
        <td id="LC653" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span>## Model choice</span></td>
      </tr>
      <tr>
        <td id="L654" class="blob-num js-line-number" data-line-number="654"></td>
        <td id="LC654" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.model <span class="pl-k">=</span> tk.StringVar()</td>
      </tr>
      <tr>
        <td id="L655" class="blob-num js-line-number" data-line-number="655"></td>
        <td id="LC655" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.model.set(<span class="pl-c1">self</span>.root_ini[<span class="pl-s"><span class="pl-pds">&quot;</span>Spectral IP model<span class="pl-pds">&quot;</span></span>])  <span class="pl-c"><span class="pl-c">#</span> set last used values</span></td>
      </tr>
      <tr>
        <td id="L656" class="blob-num js-line-number" data-line-number="656"></td>
        <td id="LC656" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> i, (txt, val) <span class="pl-k">in</span> <span class="pl-c1">enumerate</span>(models):</td>
      </tr>
      <tr>
        <td id="L657" class="blob-num js-line-number" data-line-number="657"></td>
        <td id="LC657" class="blob-code blob-code-inner js-file-line">            tk.Radiobutton(<span class="pl-c1">self</span>.frame_model, <span class="pl-v">text</span><span class="pl-k">=</span>txt, <span class="pl-v">justify</span><span class="pl-k">=</span>tk.<span class="pl-c1">LEFT</span>, <span class="pl-v">variable</span> <span class="pl-k">=</span> <span class="pl-c1">self</span>.model, <span class="pl-v">command</span> <span class="pl-k">=</span> <span class="pl-c1">self</span>.draw_rtd_check, <span class="pl-v">value</span><span class="pl-k">=</span>val).grid(<span class="pl-v">row</span><span class="pl-k">=</span>i, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W<span class="pl-k">+</span>tk.S, <span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">10</span>,<span class="pl-c1">0</span>), <span class="pl-v">pady</span><span class="pl-k">=</span>pad_radio<span class="pl-k">+</span><span class="pl-c1">2</span>)</td>
      </tr>
      <tr>
        <td id="L658" class="blob-num js-line-number" data-line-number="658"></td>
        <td id="LC658" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.draw_rtd_check()</td>
      </tr>
      <tr>
        <td id="L659" class="blob-num js-line-number" data-line-number="659"></td>
        <td id="LC659" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L660" class="blob-num js-line-number" data-line-number="660"></td>
        <td id="LC660" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">draw_rtd_check</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L661" class="blob-num js-line-number" data-line-number="661"></td>
        <td id="LC661" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L662" class="blob-num js-line-number" data-line-number="662"></td>
        <td id="LC662" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.mod_opt_frame.destroy()</td>
      </tr>
      <tr>
        <td id="L663" class="blob-num js-line-number" data-line-number="663"></td>
        <td id="LC663" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L664" class="blob-num js-line-number" data-line-number="664"></td>
        <td id="LC664" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L665" class="blob-num js-line-number" data-line-number="665"></td>
        <td id="LC665" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.mod_opt_frame <span class="pl-k">=</span> tk.Frame(<span class="pl-c1">self</span>.frame_model)</td>
      </tr>
      <tr>
        <td id="L666" class="blob-num js-line-number" data-line-number="666"></td>
        <td id="LC666" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.mod_opt_frame.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">rowspan</span><span class="pl-k">=</span><span class="pl-c1">4</span>)</td>
      </tr>
      <tr>
        <td id="L667" class="blob-num js-line-number" data-line-number="667"></td>
        <td id="LC667" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.mod_opt_frame.grid_rowconfigure(<span class="pl-c1">4</span>, <span class="pl-v">weight</span><span class="pl-k">=</span><span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L668" class="blob-num js-line-number" data-line-number="668"></td>
        <td id="LC668" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.model.get() <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>PDecomp<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L669" class="blob-num js-line-number" data-line-number="669"></td>
        <td id="LC669" class="blob-code blob-code-inner js-file-line">            poly_lab <span class="pl-k">=</span> tk.Label(<span class="pl-c1">self</span>.mod_opt_frame, <span class="pl-v">text</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Polyn order<span class="pl-pds">&quot;&quot;&quot;</span></span>, <span class="pl-v">justify</span> <span class="pl-k">=</span> tk.<span class="pl-c1">LEFT</span>, <span class="pl-v">font</span><span class="pl-k">=</span>fontz[<span class="pl-s"><span class="pl-pds">&quot;</span>normal_small<span class="pl-pds">&quot;</span></span>])</td>
      </tr>
      <tr>
        <td id="L670" class="blob-num js-line-number" data-line-number="670"></td>
        <td id="LC670" class="blob-code blob-code-inner js-file-line">            poly_lab.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">rowspan</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W<span class="pl-k">+</span>tk.N, <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">0</span>,<span class="pl-c1">0</span>), <span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">0</span>,<span class="pl-c1">10</span>))</td>
      </tr>
      <tr>
        <td id="L671" class="blob-num js-line-number" data-line-number="671"></td>
        <td id="LC671" class="blob-code blob-code-inner js-file-line">            poly_scale <span class="pl-k">=</span> tk.Scale(<span class="pl-c1">self</span>.mod_opt_frame, <span class="pl-v">variable</span><span class="pl-k">=</span><span class="pl-c1">self</span>.poly_n, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">10</span>, <span class="pl-v">length</span><span class="pl-k">=</span><span class="pl-c1">70</span>, <span class="pl-v">from_</span><span class="pl-k">=</span><span class="pl-c1">3</span>, <span class="pl-v">to</span><span class="pl-k">=</span><span class="pl-c1">6</span>, <span class="pl-v">font</span><span class="pl-k">=</span>fontz[<span class="pl-s"><span class="pl-pds">&quot;</span>normal_small<span class="pl-pds">&quot;</span></span>], <span class="pl-v">orient</span><span class="pl-k">=</span>tk.<span class="pl-c1">HORIZONTAL</span>)</td>
      </tr>
      <tr>
        <td id="L672" class="blob-num js-line-number" data-line-number="672"></td>
        <td id="LC672" class="blob-code blob-code-inner js-file-line">            poly_scale.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">rowspan</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.E<span class="pl-k">+</span>tk.N, <span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">0</span>,<span class="pl-c1">10</span>), <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">0</span>,<span class="pl-c1">0</span>))</td>
      </tr>
      <tr>
        <td id="L673" class="blob-num js-line-number" data-line-number="673"></td>
        <td id="LC673" class="blob-code blob-code-inner js-file-line">            exp_lab <span class="pl-k">=</span> tk.Label(<span class="pl-c1">self</span>.mod_opt_frame, <span class="pl-v">text</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>c exponent<span class="pl-pds">&quot;&quot;&quot;</span></span>, <span class="pl-v">justify</span> <span class="pl-k">=</span> tk.<span class="pl-c1">LEFT</span>, <span class="pl-v">font</span><span class="pl-k">=</span>fontz[<span class="pl-s"><span class="pl-pds">&quot;</span>normal_small<span class="pl-pds">&quot;</span></span>])</td>
      </tr>
      <tr>
        <td id="L674" class="blob-num js-line-number" data-line-number="674"></td>
        <td id="LC674" class="blob-code blob-code-inner js-file-line">            exp_lab.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">2</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">rowspan</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W<span class="pl-k">+</span>tk.N, <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">0</span>,<span class="pl-c1">0</span>), <span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">0</span>,<span class="pl-c1">10</span>))</td>
      </tr>
      <tr>
        <td id="L675" class="blob-num js-line-number" data-line-number="675"></td>
        <td id="LC675" class="blob-code blob-code-inner js-file-line">            exp_scale <span class="pl-k">=</span> tk.Scale(<span class="pl-c1">self</span>.mod_opt_frame, <span class="pl-v">variable</span><span class="pl-k">=</span><span class="pl-c1">self</span>.c_exp, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">10</span>, <span class="pl-v">length</span><span class="pl-k">=</span><span class="pl-c1">70</span>, <span class="pl-v">from_</span><span class="pl-k">=</span><span class="pl-c1">0.1</span>, <span class="pl-v">to</span><span class="pl-k">=</span><span class="pl-c1">1.0</span>, <span class="pl-v">resolution</span><span class="pl-k">=</span><span class="pl-c1">0.05</span>, <span class="pl-v">font</span><span class="pl-k">=</span>fontz[<span class="pl-s"><span class="pl-pds">&quot;</span>normal_small<span class="pl-pds">&quot;</span></span>], <span class="pl-v">orient</span><span class="pl-k">=</span>tk.<span class="pl-c1">HORIZONTAL</span>)</td>
      </tr>
      <tr>
        <td id="L676" class="blob-num js-line-number" data-line-number="676"></td>
        <td id="LC676" class="blob-code blob-code-inner js-file-line">            exp_scale.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">3</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">rowspan</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.E<span class="pl-k">+</span>tk.N, <span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">0</span>,<span class="pl-c1">10</span>), <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">0</span>,<span class="pl-c1">0</span>))</td>
      </tr>
      <tr>
        <td id="L677" class="blob-num js-line-number" data-line-number="677"></td>
        <td id="LC677" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.model.get() <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>ColeCole<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L678" class="blob-num js-line-number" data-line-number="678"></td>
        <td id="LC678" class="blob-code blob-code-inner js-file-line">            modes_lab <span class="pl-k">=</span> tk.Label(<span class="pl-c1">self</span>.mod_opt_frame, <span class="pl-v">text</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Nb modes<span class="pl-pds">&quot;&quot;&quot;</span></span>, <span class="pl-v">justify</span> <span class="pl-k">=</span> tk.<span class="pl-c1">LEFT</span>, <span class="pl-v">font</span><span class="pl-k">=</span>fontz[<span class="pl-s"><span class="pl-pds">&quot;</span>normal_small<span class="pl-pds">&quot;</span></span>])</td>
      </tr>
      <tr>
        <td id="L679" class="blob-num js-line-number" data-line-number="679"></td>
        <td id="LC679" class="blob-code blob-code-inner js-file-line">            modes_lab.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">rowspan</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W<span class="pl-k">+</span>tk.N, <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">0</span>,<span class="pl-c1">0</span>), <span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">0</span>,<span class="pl-c1">10</span>))</td>
      </tr>
      <tr>
        <td id="L680" class="blob-num js-line-number" data-line-number="680"></td>
        <td id="LC680" class="blob-code blob-code-inner js-file-line">            modes_scale <span class="pl-k">=</span> tk.Scale(<span class="pl-c1">self</span>.mod_opt_frame, <span class="pl-v">variable</span><span class="pl-k">=</span><span class="pl-c1">self</span>.modes_n, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">10</span>, <span class="pl-v">length</span><span class="pl-k">=</span><span class="pl-c1">70</span>, <span class="pl-v">from_</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">to</span><span class="pl-k">=</span><span class="pl-c1">3</span>, <span class="pl-v">font</span><span class="pl-k">=</span>fontz[<span class="pl-s"><span class="pl-pds">&quot;</span>normal_small<span class="pl-pds">&quot;</span></span>], <span class="pl-v">orient</span><span class="pl-k">=</span>tk.<span class="pl-c1">HORIZONTAL</span>)</td>
      </tr>
      <tr>
        <td id="L681" class="blob-num js-line-number" data-line-number="681"></td>
        <td id="LC681" class="blob-code blob-code-inner js-file-line">            modes_scale.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">rowspan</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.E<span class="pl-k">+</span>tk.N, <span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">0</span>,<span class="pl-c1">10</span>), <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">0</span>,<span class="pl-c1">0</span>))</td>
      </tr>
      <tr>
        <td id="L682" class="blob-num js-line-number" data-line-number="682"></td>
        <td id="LC682" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.model.get() <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>CCD<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L683" class="blob-num js-line-number" data-line-number="683"></td>
        <td id="LC683" class="blob-code blob-code-inner js-file-line">            modes_lab <span class="pl-k">=</span> tk.Label(<span class="pl-c1">self</span>.mod_opt_frame, <span class="pl-v">text</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-k">u</span><span class="pl-pds">&quot;</span><span class="pl-cce">\u03BB</span><span class="pl-pds">&quot;</span></span>, <span class="pl-v">justify</span> <span class="pl-k">=</span> tk.<span class="pl-c1">LEFT</span>, <span class="pl-v">font</span><span class="pl-k">=</span>fontz[<span class="pl-s"><span class="pl-pds">&quot;</span>normal_small<span class="pl-pds">&quot;</span></span>])</td>
      </tr>
      <tr>
        <td id="L684" class="blob-num js-line-number" data-line-number="684"></td>
        <td id="LC684" class="blob-code blob-code-inner js-file-line">            modes_lab.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">rowspan</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W<span class="pl-k">+</span>tk.N, <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">0</span>,<span class="pl-c1">0</span>), <span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">0</span>,<span class="pl-c1">10</span>))</td>
      </tr>
      <tr>
        <td id="L685" class="blob-num js-line-number" data-line-number="685"></td>
        <td id="LC685" class="blob-code blob-code-inner js-file-line">            modes_scale <span class="pl-k">=</span> tk.Entry(<span class="pl-c1">self</span>.mod_opt_frame, <span class="pl-v">textvariable</span><span class="pl-k">=</span><span class="pl-c1">self</span>.lamb_da, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">10</span>)</td>
      </tr>
      <tr>
        <td id="L686" class="blob-num js-line-number" data-line-number="686"></td>
        <td id="LC686" class="blob-code blob-code-inner js-file-line">            modes_scale.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">rowspan</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.E<span class="pl-k">+</span>tk.N, <span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">0</span>,<span class="pl-c1">10</span>), <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">0</span>,<span class="pl-c1">0</span>))</td>
      </tr>
      <tr>
        <td id="L687" class="blob-num js-line-number" data-line-number="687"></td>
        <td id="LC687" class="blob-code blob-code-inner js-file-line">            exp_lab <span class="pl-k">=</span> tk.Label(<span class="pl-c1">self</span>.mod_opt_frame, <span class="pl-v">text</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>c exponent<span class="pl-pds">&quot;&quot;&quot;</span></span>, <span class="pl-v">justify</span> <span class="pl-k">=</span> tk.<span class="pl-c1">LEFT</span>, <span class="pl-v">font</span><span class="pl-k">=</span>fontz[<span class="pl-s"><span class="pl-pds">&quot;</span>normal_small<span class="pl-pds">&quot;</span></span>])</td>
      </tr>
      <tr>
        <td id="L688" class="blob-num js-line-number" data-line-number="688"></td>
        <td id="LC688" class="blob-code blob-code-inner js-file-line">            exp_lab.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">2</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">rowspan</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W<span class="pl-k">+</span>tk.N, <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">0</span>,<span class="pl-c1">0</span>), <span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">0</span>,<span class="pl-c1">10</span>))</td>
      </tr>
      <tr>
        <td id="L689" class="blob-num js-line-number" data-line-number="689"></td>
        <td id="LC689" class="blob-code blob-code-inner js-file-line">            exp_scale <span class="pl-k">=</span> tk.Scale(<span class="pl-c1">self</span>.mod_opt_frame, <span class="pl-v">variable</span><span class="pl-k">=</span><span class="pl-c1">self</span>.c_exp, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">10</span>, <span class="pl-v">length</span><span class="pl-k">=</span><span class="pl-c1">70</span>, <span class="pl-v">from_</span><span class="pl-k">=</span><span class="pl-c1">0.1</span>, <span class="pl-v">to</span><span class="pl-k">=</span><span class="pl-c1">1.0</span>, <span class="pl-v">resolution</span><span class="pl-k">=</span><span class="pl-c1">0.05</span>, <span class="pl-v">font</span><span class="pl-k">=</span>fontz[<span class="pl-s"><span class="pl-pds">&quot;</span>normal_small<span class="pl-pds">&quot;</span></span>], <span class="pl-v">orient</span><span class="pl-k">=</span>tk.<span class="pl-c1">HORIZONTAL</span>)</td>
      </tr>
      <tr>
        <td id="L690" class="blob-num js-line-number" data-line-number="690"></td>
        <td id="LC690" class="blob-code blob-code-inner js-file-line">            exp_scale.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">3</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">rowspan</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.E<span class="pl-k">+</span>tk.N, <span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">0</span>,<span class="pl-c1">10</span>), <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">0</span>,<span class="pl-c1">0</span>))</td>
      </tr>
      <tr>
        <td id="L691" class="blob-num js-line-number" data-line-number="691"></td>
        <td id="LC691" class="blob-code blob-code-inner js-file-line"> </td>
      </tr>
      <tr>
        <td id="L692" class="blob-num js-line-number" data-line-number="692"></td>
        <td id="LC692" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L693" class="blob-num js-line-number" data-line-number="693"></td>
        <td id="LC693" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>==============================================================================</span></td>
      </tr>
      <tr>
        <td id="L694" class="blob-num js-line-number" data-line-number="694"></td>
        <td id="LC694" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Run Exit Options</span></td>
      </tr>
      <tr>
        <td id="L695" class="blob-num js-line-number" data-line-number="695"></td>
        <td id="LC695" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>==============================================================================</span></td>
      </tr>
      <tr>
        <td id="L696" class="blob-num js-line-number" data-line-number="696"></td>
        <td id="LC696" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">run_exit</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L697" class="blob-num js-line-number" data-line-number="697"></td>
        <td id="LC697" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> i, (k, v) <span class="pl-k">in</span> <span class="pl-c1">enumerate</span>(<span class="pl-c1">self</span>.run_options.items()):</td>
      </tr>
      <tr>
        <td id="L698" class="blob-num js-line-number" data-line-number="698"></td>
        <td id="LC698" class="blob-code blob-code-inner js-file-line">            tk.Checkbutton(<span class="pl-c1">self</span>.frame_ruex, <span class="pl-v">text</span><span class="pl-k">=</span>k, <span class="pl-v">variable</span><span class="pl-k">=</span>v).grid(<span class="pl-v">row</span><span class="pl-k">=</span>i, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">10</span>,<span class="pl-c1">0</span>), <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W<span class="pl-k">+</span>tk.N<span class="pl-k">+</span>tk.S)</td>
      </tr>
      <tr>
        <td id="L699" class="blob-num js-line-number" data-line-number="699"></td>
        <td id="LC699" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.run_options[k].set(<span class="pl-c1">self</span>.root_ini[k]) <span class="pl-c"><span class="pl-c">#</span> set last used values</span></td>
      </tr>
      <tr>
        <td id="L700" class="blob-num js-line-number" data-line-number="700"></td>
        <td id="LC700" class="blob-code blob-code-inner js-file-line">        tk.Button(<span class="pl-c1">self</span>.frame_ruex, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">14</span>, <span class="pl-v">text</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Options<span class="pl-pds">&quot;</span></span>, <span class="pl-v">fg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>black<span class="pl-pds">&#39;</span></span>, <span class="pl-v">bg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>gray97<span class="pl-pds">&#39;</span></span>, <span class="pl-v">font</span><span class="pl-k">=</span>fontz[<span class="pl-s"><span class="pl-pds">&quot;</span>bold<span class="pl-pds">&quot;</span></span>], <span class="pl-v">relief</span><span class="pl-k">=</span>tk.<span class="pl-c1">GROOVE</span>,</td>
      </tr>
      <tr>
        <td id="L701" class="blob-num js-line-number" data-line-number="701"></td>
        <td id="LC701" class="blob-code blob-code-inner js-file-line">                            <span class="pl-v">command</span> <span class="pl-k">=</span> <span class="pl-c1">self</span>.make_options).grid(<span class="pl-v">row</span><span class="pl-k">=</span>i<span class="pl-k">+</span><span class="pl-c1">1</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">rowspan</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.N<span class="pl-k">+</span>tk.E<span class="pl-k">+</span>tk.W<span class="pl-k">+</span>tk.S, <span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">10</span>,<span class="pl-c1">5</span>), <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">0</span>,<span class="pl-c1">10</span>))</td>
      </tr>
      <tr>
        <td id="L702" class="blob-num js-line-number" data-line-number="702"></td>
        <td id="LC702" class="blob-code blob-code-inner js-file-line">        tk.Button(<span class="pl-c1">self</span>.frame_ruex, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">14</span>, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">text</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>RUN<span class="pl-pds">&quot;</span></span>, <span class="pl-v">fg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>blue<span class="pl-pds">&#39;</span></span>, <span class="pl-v">bg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>gray97<span class="pl-pds">&#39;</span></span>, <span class="pl-v">font</span><span class="pl-k">=</span>fontz[<span class="pl-s"><span class="pl-pds">&quot;</span>bold<span class="pl-pds">&quot;</span></span>], <span class="pl-v">relief</span><span class="pl-k">=</span>tk.<span class="pl-c1">GROOVE</span>,</td>
      </tr>
      <tr>
        <td id="L703" class="blob-num js-line-number" data-line-number="703"></td>
        <td id="LC703" class="blob-code blob-code-inner js-file-line">                            <span class="pl-v">command</span> <span class="pl-k">=</span> <span class="pl-c1">self</span>.run_inversion).grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">rowspan</span><span class="pl-k">=</span><span class="pl-c1">2</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.N<span class="pl-k">+</span>tk.E<span class="pl-k">+</span>tk.S, <span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">5</span>,<span class="pl-c1">10</span>), <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">5</span>,<span class="pl-c1">0</span>), <span class="pl-v">ipadx</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">ipady</span><span class="pl-k">=</span><span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L704" class="blob-num js-line-number" data-line-number="704"></td>
        <td id="LC704" class="blob-code blob-code-inner js-file-line">        tk.Button(<span class="pl-c1">self</span>.frame_ruex, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">14</span>, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">text</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>EXIT<span class="pl-pds">&quot;</span></span>, <span class="pl-v">fg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>red<span class="pl-pds">&#39;</span></span>, <span class="pl-v">bg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>gray97<span class="pl-pds">&#39;</span></span>, <span class="pl-v">font</span><span class="pl-k">=</span>fontz[<span class="pl-s"><span class="pl-pds">&quot;</span>bold<span class="pl-pds">&quot;</span></span>], <span class="pl-v">relief</span><span class="pl-k">=</span>tk.<span class="pl-c1">GROOVE</span>,</td>
      </tr>
      <tr>
        <td id="L705" class="blob-num js-line-number" data-line-number="705"></td>
        <td id="LC705" class="blob-code blob-code-inner js-file-line">                            <span class="pl-v">command</span> <span class="pl-k">=</span> <span class="pl-c1">self</span>.master.destroy).grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">2</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">rowspan</span><span class="pl-k">=</span><span class="pl-c1">2</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.S<span class="pl-k">+</span>tk.E<span class="pl-k">+</span>tk.N, <span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">5</span>,<span class="pl-c1">10</span>), <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">0</span>,<span class="pl-c1">10</span>))</td>
      </tr>
      <tr>
        <td id="L706" class="blob-num js-line-number" data-line-number="706"></td>
        <td id="LC706" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L707" class="blob-num js-line-number" data-line-number="707"></td>
        <td id="LC707" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">make_options</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">from_root</span><span class="pl-k">=</span><span class="pl-c1">False</span>):</td>
      </tr>
      <tr>
        <td id="L708" class="blob-num js-line-number" data-line-number="708"></td>
        <td id="LC708" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>: <span class="pl-c1">self</span>.top_checkbox.destroy()</td>
      </tr>
      <tr>
        <td id="L709" class="blob-num js-line-number" data-line-number="709"></td>
        <td id="LC709" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span>: <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L710" class="blob-num js-line-number" data-line-number="710"></td>
        <td id="LC710" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L711" class="blob-num js-line-number" data-line-number="711"></td>
        <td id="LC711" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> Select all or none functions</span></td>
      </tr>
      <tr>
        <td id="L712" class="blob-num js-line-number" data-line-number="712"></td>
        <td id="LC712" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">def</span> <span class="pl-en">select_all</span>(): <span class="pl-c"><span class="pl-c">#</span> self expl</span></td>
      </tr>
      <tr>
        <td id="L713" class="blob-num js-line-number" data-line-number="713"></td>
        <td id="LC713" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> v <span class="pl-k">in</span> <span class="pl-c1">list</span>(<span class="pl-c1">self</span>.save_options.values()):</td>
      </tr>
      <tr>
        <td id="L714" class="blob-num js-line-number" data-line-number="714"></td>
        <td id="LC714" class="blob-code blob-code-inner js-file-line">                v.set(<span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L715" class="blob-num js-line-number" data-line-number="715"></td>
        <td id="LC715" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">def</span> <span class="pl-en">select_none</span>(): <span class="pl-c"><span class="pl-c">#</span> self expl</span></td>
      </tr>
      <tr>
        <td id="L716" class="blob-num js-line-number" data-line-number="716"></td>
        <td id="LC716" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> v <span class="pl-k">in</span> <span class="pl-c1">list</span>(<span class="pl-c1">self</span>.save_options.values()):</td>
      </tr>
      <tr>
        <td id="L717" class="blob-num js-line-number" data-line-number="717"></td>
        <td id="LC717" class="blob-code blob-code-inner js-file-line">                v.set(<span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L718" class="blob-num js-line-number" data-line-number="718"></td>
        <td id="LC718" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-k">not</span> from_root:</td>
      </tr>
      <tr>
        <td id="L719" class="blob-num js-line-number" data-line-number="719"></td>
        <td id="LC719" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.top_checkbox <span class="pl-k">=</span> tk.Toplevel(<span class="pl-c1">self</span>.master)</td>
      </tr>
      <tr>
        <td id="L720" class="blob-num js-line-number" data-line-number="720"></td>
        <td id="LC720" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.top_checkbox.title(<span class="pl-s"><span class="pl-pds">&quot;</span>Save options<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L721" class="blob-num js-line-number" data-line-number="721"></td>
        <td id="LC721" class="blob-code blob-code-inner js-file-line">            frame_checkbox <span class="pl-k">=</span> tk.LabelFrame(<span class="pl-c1">self</span>.top_checkbox, <span class="pl-v">text</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Check items to save<span class="pl-pds">&quot;</span></span>, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">200</span>, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">4</span>, <span class="pl-v">font</span><span class="pl-k">=</span>fontz[<span class="pl-s"><span class="pl-pds">&quot;</span>bold<span class="pl-pds">&quot;</span></span>])</td>
      </tr>
      <tr>
        <td id="L722" class="blob-num js-line-number" data-line-number="722"></td>
        <td id="LC722" class="blob-code blob-code-inner js-file-line">            frame_checkbox.grid(<span class="pl-v">row</span> <span class="pl-k">=</span> <span class="pl-c1">0</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>,<span class="pl-v">sticky</span><span class="pl-k">=</span>tk.S<span class="pl-k">+</span>tk.W<span class="pl-k">+</span>tk.E<span class="pl-k">+</span>tk.N, <span class="pl-v">padx</span><span class="pl-k">=</span><span class="pl-c1">10</span>, <span class="pl-v">pady</span><span class="pl-k">=</span><span class="pl-c1">10</span>)</td>
      </tr>
      <tr>
        <td id="L723" class="blob-num js-line-number" data-line-number="723"></td>
        <td id="LC723" class="blob-code blob-code-inner js-file-line">            tk.Button(frame_checkbox, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">15</span>, <span class="pl-v">text</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Check all<span class="pl-pds">&quot;</span></span>, <span class="pl-v">command</span><span class="pl-k">=</span>select_all, <span class="pl-v">bg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>gray97<span class="pl-pds">&#39;</span></span>, <span class="pl-v">font</span><span class="pl-k">=</span>fontz[<span class="pl-s"><span class="pl-pds">&quot;</span>normal_small<span class="pl-pds">&quot;</span></span>], <span class="pl-v">relief</span><span class="pl-k">=</span>tk.<span class="pl-c1">GROOVE</span>).grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W, <span class="pl-v">pady</span><span class="pl-k">=</span><span class="pl-c1">5</span>, <span class="pl-v">padx</span><span class="pl-k">=</span><span class="pl-c1">10</span>)</td>
      </tr>
      <tr>
        <td id="L724" class="blob-num js-line-number" data-line-number="724"></td>
        <td id="LC724" class="blob-code blob-code-inner js-file-line">            tk.Button(frame_checkbox, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">15</span>, <span class="pl-v">text</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Check none<span class="pl-pds">&quot;</span></span>, <span class="pl-v">command</span><span class="pl-k">=</span>select_none, <span class="pl-v">bg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>gray97<span class="pl-pds">&#39;</span></span>, <span class="pl-v">font</span><span class="pl-k">=</span>fontz[<span class="pl-s"><span class="pl-pds">&quot;</span>normal_small<span class="pl-pds">&quot;</span></span>], <span class="pl-v">relief</span><span class="pl-k">=</span>tk.<span class="pl-c1">GROOVE</span>).grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.E, <span class="pl-v">pady</span><span class="pl-k">=</span><span class="pl-c1">5</span>, <span class="pl-v">padx</span><span class="pl-k">=</span><span class="pl-c1">10</span>)</td>
      </tr>
      <tr>
        <td id="L725" class="blob-num js-line-number" data-line-number="725"></td>
        <td id="LC725" class="blob-code blob-code-inner js-file-line">            button <span class="pl-k">=</span> tk.Button(frame_checkbox, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">2</span>, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">20</span>, <span class="pl-v">text</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>OK<span class="pl-pds">&quot;</span></span>, <span class="pl-v">bg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>gray97<span class="pl-pds">&#39;</span></span>, <span class="pl-v">font</span><span class="pl-k">=</span>fontz[<span class="pl-s"><span class="pl-pds">&quot;</span>bold<span class="pl-pds">&quot;</span></span>], <span class="pl-v">command</span><span class="pl-k">=</span><span class="pl-c1">self</span>.top_checkbox.destroy, <span class="pl-v">relief</span><span class="pl-k">=</span>tk.<span class="pl-c1">GROOVE</span>)</td>
      </tr>
      <tr>
        <td id="L726" class="blob-num js-line-number" data-line-number="726"></td>
        <td id="LC726" class="blob-code blob-code-inner js-file-line">            button.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">len</span>(<span class="pl-c1">self</span>.save_options)<span class="pl-k">+</span><span class="pl-c1">2</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">columnspan</span><span class="pl-k">=</span><span class="pl-c1">2</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W<span class="pl-k">+</span>tk.E, <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">10</span>,<span class="pl-c1">10</span>), <span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">20</span>,<span class="pl-c1">20</span>))</td>
      </tr>
      <tr>
        <td id="L727" class="blob-num js-line-number" data-line-number="727"></td>
        <td id="LC727" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> i, (k, v) <span class="pl-k">in</span> <span class="pl-c1">enumerate</span>(<span class="pl-c1">sorted</span>(<span class="pl-c1">self</span>.save_options.items())):</td>
      </tr>
      <tr>
        <td id="L728" class="blob-num js-line-number" data-line-number="728"></td>
        <td id="LC728" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> from_root:</td>
      </tr>
      <tr>
        <td id="L729" class="blob-num js-line-number" data-line-number="729"></td>
        <td id="LC729" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.save_options[k].set(<span class="pl-c1">self</span>.root_ini[k])</td>
      </tr>
      <tr>
        <td id="L730" class="blob-num js-line-number" data-line-number="730"></td>
        <td id="LC730" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-k">not</span> from_root:</td>
      </tr>
      <tr>
        <td id="L731" class="blob-num js-line-number" data-line-number="731"></td>
        <td id="LC731" class="blob-code blob-code-inner js-file-line">                tk.Checkbutton(frame_checkbox, <span class="pl-v">text</span><span class="pl-k">=</span>k, <span class="pl-v">variable</span><span class="pl-k">=</span>v).grid(<span class="pl-v">row</span><span class="pl-k">=</span>i<span class="pl-k">+</span><span class="pl-c1">1</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W<span class="pl-k">+</span>tk.N<span class="pl-k">+</span>tk.S,<span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">10</span>,<span class="pl-c1">10</span>),<span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">5</span>,<span class="pl-c1">0</span>))</td>
      </tr>
      <tr>
        <td id="L732" class="blob-num js-line-number" data-line-number="732"></td>
        <td id="LC732" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L733" class="blob-num js-line-number" data-line-number="733"></td>
        <td id="LC733" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>==============================================================================</span></td>
      </tr>
      <tr>
        <td id="L734" class="blob-num js-line-number" data-line-number="734"></td>
        <td id="LC734" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Plotting</span></td>
      </tr>
      <tr>
        <td id="L735" class="blob-num js-line-number" data-line-number="735"></td>
        <td id="LC735" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>==============================================================================</span></td>
      </tr>
      <tr>
        <td id="L736" class="blob-num js-line-number" data-line-number="736"></td>
        <td id="LC736" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">set_plot_par</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>): <span class="pl-c"><span class="pl-c">#</span> Setting up plotting parameters</span></td>
      </tr>
      <tr>
        <td id="L737" class="blob-num js-line-number" data-line-number="737"></td>
        <td id="LC737" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L738" class="blob-num js-line-number" data-line-number="738"></td>
        <td id="LC738" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\n</span>Loading plot parameters<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L739" class="blob-num js-line-number" data-line-number="739"></td>
        <td id="LC739" class="blob-code blob-code-inner js-file-line">            rcParams.update(iR.plot_par())</td>
      </tr>
      <tr>
        <td id="L740" class="blob-num js-line-number" data-line-number="740"></td>
        <td id="LC740" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>Plot parameters successfully loaded<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L741" class="blob-num js-line-number" data-line-number="741"></td>
        <td id="LC741" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L742" class="blob-num js-line-number" data-line-number="742"></td>
        <td id="LC742" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>Plot parameters not found, using default values<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L743" class="blob-num js-line-number" data-line-number="743"></td>
        <td id="LC743" class="blob-code blob-code-inner js-file-line">        stdout.flush()</td>
      </tr>
      <tr>
        <td id="L744" class="blob-num js-line-number" data-line-number="744"></td>
        <td id="LC744" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L745" class="blob-num js-line-number" data-line-number="745"></td>
        <td id="LC745" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">preview_data</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L746" class="blob-num js-line-number" data-line-number="746"></td>
        <td id="LC746" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>        try:</span></td>
      </tr>
      <tr>
        <td id="L747" class="blob-num js-line-number" data-line-number="747"></td>
        <td id="LC747" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> i <span class="pl-k">in</span> <span class="pl-c1">self</span>.text_files.curselection():</td>
      </tr>
      <tr>
        <td id="L748" class="blob-num js-line-number" data-line-number="748"></td>
        <td id="LC748" class="blob-code blob-code-inner js-file-line">                sel <span class="pl-k">=</span> <span class="pl-c1">str</span>(<span class="pl-c1">self</span>.open_files[i])</td>
      </tr>
      <tr>
        <td id="L749" class="blob-num js-line-number" data-line-number="749"></td>
        <td id="LC749" class="blob-code blob-code-inner js-file-line">                fn <span class="pl-k">=</span> sel.split(<span class="pl-s"><span class="pl-pds">&quot;</span>/<span class="pl-pds">&quot;</span></span>)[<span class="pl-k">-</span><span class="pl-c1">1</span>].split(<span class="pl-s"><span class="pl-pds">&quot;</span>.<span class="pl-pds">&quot;</span></span>)[<span class="pl-c1">0</span>]</td>
      </tr>
      <tr>
        <td id="L750" class="blob-num js-line-number" data-line-number="750"></td>
        <td id="LC750" class="blob-code blob-code-inner js-file-line">                fig_data <span class="pl-k">=</span> iR.plot_data(sel, <span class="pl-c1">self</span>.head.get(), <span class="pl-c1">self</span>.units.get())</td>
      </tr>
      <tr>
        <td id="L751" class="blob-num js-line-number" data-line-number="751"></td>
        <td id="LC751" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.plot_window(fig_data, <span class="pl-s"><span class="pl-pds">&quot;</span>Data preview: <span class="pl-pds">&quot;</span></span><span class="pl-k">+</span>fn)</td>
      </tr>
      <tr>
        <td id="L752" class="blob-num js-line-number" data-line-number="752"></td>
        <td id="LC752" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>        except:</span></td>
      </tr>
      <tr>
        <td id="L753" class="blob-num js-line-number" data-line-number="753"></td>
        <td id="LC753" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>            tkinter.messagebox.showwarning(&quot;Preview error&quot;,</span></td>
      </tr>
      <tr>
        <td id="L754" class="blob-num js-line-number" data-line-number="754"></td>
        <td id="LC754" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>                                     &quot;Can&#39;t draw data\nImport and select at least one data file first&quot;, parent=self.master)</span></td>
      </tr>
      <tr>
        <td id="L755" class="blob-num js-line-number" data-line-number="755"></td>
        <td id="LC755" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L756" class="blob-num js-line-number" data-line-number="756"></td>
        <td id="LC756" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">plot_diagnostic</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">which</span>):</td>
      </tr>
      <tr>
        <td id="L757" class="blob-num js-line-number" data-line-number="757"></td>
        <td id="LC757" class="blob-code blob-code-inner js-file-line">        f_n <span class="pl-k">=</span> <span class="pl-c1">self</span>.var_review.get()</td>
      </tr>
      <tr>
        <td id="L758" class="blob-num js-line-number" data-line-number="758"></td>
        <td id="LC758" class="blob-code blob-code-inner js-file-line">        sol <span class="pl-k">=</span> <span class="pl-c1">self</span>.all_results[f_n][<span class="pl-s"><span class="pl-pds">&quot;</span>sol<span class="pl-pds">&quot;</span></span>]</td>
      </tr>
      <tr>
        <td id="L759" class="blob-num js-line-number" data-line-number="759"></td>
        <td id="LC759" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L760" class="blob-num js-line-number" data-line-number="760"></td>
        <td id="LC760" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> which <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>traces<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L761" class="blob-num js-line-number" data-line-number="761"></td>
        <td id="LC761" class="blob-code blob-code-inner js-file-line">                trace_plot <span class="pl-k">=</span> sol.plot_traces(<span class="pl-v">save</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L762" class="blob-num js-line-number" data-line-number="762"></td>
        <td id="LC762" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.plot_window(trace_plot, <span class="pl-s"><span class="pl-pds">&quot;</span>Parameter traces: <span class="pl-pds">&quot;</span></span><span class="pl-k">+</span>f_n)</td>
      </tr>
      <tr>
        <td id="L763" class="blob-num js-line-number" data-line-number="763"></td>
        <td id="LC763" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> which <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>histo<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L764" class="blob-num js-line-number" data-line-number="764"></td>
        <td id="LC764" class="blob-code blob-code-inner js-file-line">                histo_plot <span class="pl-k">=</span> sol.plot_histograms(<span class="pl-v">save</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L765" class="blob-num js-line-number" data-line-number="765"></td>
        <td id="LC765" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.plot_window(histo_plot, <span class="pl-s"><span class="pl-pds">&quot;</span>Parameter histograms: <span class="pl-pds">&quot;</span></span><span class="pl-k">+</span>f_n)</td>
      </tr>
      <tr>
        <td id="L766" class="blob-num js-line-number" data-line-number="766"></td>
        <td id="LC766" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> which <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>autocorr<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L767" class="blob-num js-line-number" data-line-number="767"></td>
        <td id="LC767" class="blob-code blob-code-inner js-file-line">                autocorr_plot <span class="pl-k">=</span> sol.plot_autocorrelation(<span class="pl-v">save</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L768" class="blob-num js-line-number" data-line-number="768"></td>
        <td id="LC768" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.plot_window(autocorr_plot, <span class="pl-s"><span class="pl-pds">&quot;</span>Parameter autocorrelation: <span class="pl-pds">&quot;</span></span><span class="pl-k">+</span>f_n)</td>
      </tr>
      <tr>
        <td id="L769" class="blob-num js-line-number" data-line-number="769"></td>
        <td id="LC769" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> which <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>geweke<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L770" class="blob-num js-line-number" data-line-number="770"></td>
        <td id="LC770" class="blob-code blob-code-inner js-file-line">                geweke_plot <span class="pl-k">=</span> sol.plot_scores(<span class="pl-v">save</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L771" class="blob-num js-line-number" data-line-number="771"></td>
        <td id="LC771" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.plot_window(geweke_plot, <span class="pl-s"><span class="pl-pds">&quot;</span>Geweke scores: <span class="pl-pds">&quot;</span></span><span class="pl-k">+</span>f_n)</td>
      </tr>
      <tr>
        <td id="L772" class="blob-num js-line-number" data-line-number="772"></td>
        <td id="LC772" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> which <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>summary<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L773" class="blob-num js-line-number" data-line-number="773"></td>
        <td id="LC773" class="blob-code blob-code-inner js-file-line">                summa_plot <span class="pl-k">=</span> sol.plot_summary(<span class="pl-v">save</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L774" class="blob-num js-line-number" data-line-number="774"></td>
        <td id="LC774" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.plot_window(summa_plot, <span class="pl-s"><span class="pl-pds">&quot;</span>Parameter summary: <span class="pl-pds">&quot;</span></span><span class="pl-k">+</span>f_n)</td>
      </tr>
      <tr>
        <td id="L775" class="blob-num js-line-number" data-line-number="775"></td>
        <td id="LC775" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> which <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>deviance<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L776" class="blob-num js-line-number" data-line-number="776"></td>
        <td id="LC776" class="blob-code blob-code-inner js-file-line">                devi_plot <span class="pl-k">=</span> sol.plot_model_deviance(<span class="pl-v">save</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L777" class="blob-num js-line-number" data-line-number="777"></td>
        <td id="LC777" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.plot_window(devi_plot, <span class="pl-s"><span class="pl-pds">&quot;</span>Model deviance: <span class="pl-pds">&quot;</span></span><span class="pl-k">+</span>f_n)</td>
      </tr>
      <tr>
        <td id="L778" class="blob-num js-line-number" data-line-number="778"></td>
        <td id="LC778" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> which <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>logp<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L779" class="blob-num js-line-number" data-line-number="779"></td>
        <td id="LC779" class="blob-code blob-code-inner js-file-line">                logp_plot <span class="pl-k">=</span> sol.plot_log_likelihood(<span class="pl-v">save</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L780" class="blob-num js-line-number" data-line-number="780"></td>
        <td id="LC780" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.plot_window(logp_plot, <span class="pl-s"><span class="pl-pds">&quot;</span>Log-likelihood: <span class="pl-pds">&quot;</span></span><span class="pl-k">+</span>f_n)</td>
      </tr>
      <tr>
        <td id="L781" class="blob-num js-line-number" data-line-number="781"></td>
        <td id="LC781" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> which <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>hexbin<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L782" class="blob-num js-line-number" data-line-number="782"></td>
        <td id="LC782" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">try</span>: <span class="pl-c1">self</span>.top_bivar.destroy()</td>
      </tr>
      <tr>
        <td id="L783" class="blob-num js-line-number" data-line-number="783"></td>
        <td id="LC783" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">except</span>: <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L784" class="blob-num js-line-number" data-line-number="784"></td>
        <td id="LC784" class="blob-code blob-code-inner js-file-line">                hex_plot <span class="pl-k">=</span> sol.plot_hexbin(<span class="pl-c1">self</span>.biv1.get(), <span class="pl-c1">self</span>.biv2.get(), <span class="pl-v">save</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L785" class="blob-num js-line-number" data-line-number="785"></td>
        <td id="LC785" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.plot_window(hex_plot, <span class="pl-s"><span class="pl-pds">&quot;</span>Hexagonal binning: <span class="pl-pds">&quot;</span></span><span class="pl-k">+</span>f_n)</td>
      </tr>
      <tr>
        <td id="L786" class="blob-num js-line-number" data-line-number="786"></td>
        <td id="LC786" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> which <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>KDE<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L787" class="blob-num js-line-number" data-line-number="787"></td>
        <td id="LC787" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">try</span>: <span class="pl-c1">self</span>.top_bivar.destroy()</td>
      </tr>
      <tr>
        <td id="L788" class="blob-num js-line-number" data-line-number="788"></td>
        <td id="LC788" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">except</span>: <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L789" class="blob-num js-line-number" data-line-number="789"></td>
        <td id="LC789" class="blob-code blob-code-inner js-file-line">                kde_plot <span class="pl-k">=</span> sol.plot_KDE(<span class="pl-c1">self</span>.biv1.get(), <span class="pl-c1">self</span>.biv2.get(), <span class="pl-v">save</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L790" class="blob-num js-line-number" data-line-number="790"></td>
        <td id="LC790" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.plot_window(kde_plot, <span class="pl-s"><span class="pl-pds">&quot;</span>Bivariate KDE: <span class="pl-pds">&quot;</span></span><span class="pl-k">+</span>f_n)</td>
      </tr>
      <tr>
        <td id="L791" class="blob-num js-line-number" data-line-number="791"></td>
        <td id="LC791" class="blob-code blob-code-inner js-file-line">            stdout.flush()</td>
      </tr>
      <tr>
        <td id="L792" class="blob-num js-line-number" data-line-number="792"></td>
        <td id="LC792" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L793" class="blob-num js-line-number" data-line-number="793"></td>
        <td id="LC793" class="blob-code blob-code-inner js-file-line">            tkinter.messagebox.showwarning(<span class="pl-s"><span class="pl-pds">&quot;</span>Error analyzing results<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>Error<span class="pl-cce">\n</span>Problem with inversion results<span class="pl-cce">\n</span>Try adding iterations<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L794" class="blob-num js-line-number" data-line-number="794"></td>
        <td id="LC794" class="blob-code blob-code-inner js-file-line">                                     <span class="pl-v">parent</span><span class="pl-k">=</span><span class="pl-c1">self</span>.master)</td>
      </tr>
      <tr>
        <td id="L795" class="blob-num js-line-number" data-line-number="795"></td>
        <td id="LC795" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L796" class="blob-num js-line-number" data-line-number="796"></td>
        <td id="LC796" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">plot_window</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">fig</span>, <span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span>):</td>
      </tr>
      <tr>
        <td id="L797" class="blob-num js-line-number" data-line-number="797"></td>
        <td id="LC797" class="blob-code blob-code-inner js-file-line">        top_fig <span class="pl-k">=</span> tk.Toplevel()</td>
      </tr>
      <tr>
        <td id="L798" class="blob-num js-line-number" data-line-number="798"></td>
        <td id="LC798" class="blob-code blob-code-inner js-file-line">        top_fig.lift()</td>
      </tr>
      <tr>
        <td id="L799" class="blob-num js-line-number" data-line-number="799"></td>
        <td id="LC799" class="blob-code blob-code-inner js-file-line">        top_fig.title(name)</td>
      </tr>
      <tr>
        <td id="L800" class="blob-num js-line-number" data-line-number="800"></td>
        <td id="LC800" class="blob-code blob-code-inner js-file-line">        top_fig.rowconfigure(<span class="pl-c1">1</span>, <span class="pl-v">weight</span><span class="pl-k">=</span><span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L801" class="blob-num js-line-number" data-line-number="801"></td>
        <td id="LC801" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">def</span> <span class="pl-en">_quit</span>():</td>
      </tr>
      <tr>
        <td id="L802" class="blob-num js-line-number" data-line-number="802"></td>
        <td id="LC802" class="blob-code blob-code-inner js-file-line">            top_fig.destroy()</td>
      </tr>
      <tr>
        <td id="L803" class="blob-num js-line-number" data-line-number="803"></td>
        <td id="LC803" class="blob-code blob-code-inner js-file-line">        canvas <span class="pl-k">=</span> FigureCanvasTkAgg(fig, <span class="pl-v">master</span><span class="pl-k">=</span>top_fig)</td>
      </tr>
      <tr>
        <td id="L804" class="blob-num js-line-number" data-line-number="804"></td>
        <td id="LC804" class="blob-code blob-code-inner js-file-line">        canvas.show()</td>
      </tr>
      <tr>
        <td id="L805" class="blob-num js-line-number" data-line-number="805"></td>
        <td id="LC805" class="blob-code blob-code-inner js-file-line">        canvas.get_tk_widget().grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">columnspan</span> <span class="pl-k">=</span> <span class="pl-c1">3</span>, <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">15</span>,<span class="pl-c1">15</span>), <span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">25</span>,<span class="pl-c1">25</span>), <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.N<span class="pl-k">+</span>tk.S<span class="pl-k">+</span>tk.E<span class="pl-k">+</span>tk.W)</td>
      </tr>
      <tr>
        <td id="L806" class="blob-num js-line-number" data-line-number="806"></td>
        <td id="LC806" class="blob-code blob-code-inner js-file-line">        button <span class="pl-k">=</span> tk.Button(top_fig, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">20</span>, <span class="pl-v">text</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Dismiss<span class="pl-pds">&quot;</span></span>, <span class="pl-v">bg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>gray97<span class="pl-pds">&#39;</span></span>, <span class="pl-v">command</span><span class="pl-k">=</span>_quit, <span class="pl-v">relief</span><span class="pl-k">=</span>tk.<span class="pl-c1">GROOVE</span>)</td>
      </tr>
      <tr>
        <td id="L807" class="blob-num js-line-number" data-line-number="807"></td>
        <td id="LC807" class="blob-code blob-code-inner js-file-line">        button.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">2</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">columnspan</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W, <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">10</span>,<span class="pl-c1">10</span>), <span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">20</span>,<span class="pl-c1">20</span>))</td>
      </tr>
      <tr>
        <td id="L808" class="blob-num js-line-number" data-line-number="808"></td>
        <td id="LC808" class="blob-code blob-code-inner js-file-line">        toolbar_frame <span class="pl-k">=</span> tk.Frame(top_fig)</td>
      </tr>
      <tr>
        <td id="L809" class="blob-num js-line-number" data-line-number="809"></td>
        <td id="LC809" class="blob-code blob-code-inner js-file-line">        toolbar_frame.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">0</span>,<span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>,<span class="pl-v">columnspan</span><span class="pl-k">=</span><span class="pl-c1">2</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W<span class="pl-k">+</span>tk.E)</td>
      </tr>
      <tr>
        <td id="L810" class="blob-num js-line-number" data-line-number="810"></td>
        <td id="LC810" class="blob-code blob-code-inner js-file-line">        NavigationToolbar2TkAgg( canvas, toolbar_frame )</td>
      </tr>
      <tr>
        <td id="L811" class="blob-num js-line-number" data-line-number="811"></td>
        <td id="LC811" class="blob-code blob-code-inner js-file-line">        top_fig.resizable(<span class="pl-v">width</span><span class="pl-k">=</span>tk.<span class="pl-c1">FALSE</span>, <span class="pl-v">height</span><span class="pl-k">=</span>tk.<span class="pl-c1">FALSE</span>)</td>
      </tr>
      <tr>
        <td id="L812" class="blob-num js-line-number" data-line-number="812"></td>
        <td id="LC812" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L813" class="blob-num js-line-number" data-line-number="813"></td>
        <td id="LC813" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">plot_fit_now</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L814" class="blob-num js-line-number" data-line-number="814"></td>
        <td id="LC814" class="blob-code blob-code-inner js-file-line">        f_n <span class="pl-k">=</span> <span class="pl-c1">self</span>.var_review.get()</td>
      </tr>
      <tr>
        <td id="L815" class="blob-num js-line-number" data-line-number="815"></td>
        <td id="LC815" class="blob-code blob-code-inner js-file-line">        sol <span class="pl-k">=</span> <span class="pl-c1">self</span>.all_results[f_n][<span class="pl-s"><span class="pl-pds">&quot;</span>sol<span class="pl-pds">&quot;</span></span>]</td>
      </tr>
      <tr>
        <td id="L816" class="blob-num js-line-number" data-line-number="816"></td>
        <td id="LC816" class="blob-code blob-code-inner js-file-line">        fig_fit <span class="pl-k">=</span> sol.plot_fit(<span class="pl-v">save</span><span class="pl-k">=</span><span class="pl-c1">False</span>, <span class="pl-v">draw</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L817" class="blob-num js-line-number" data-line-number="817"></td>
        <td id="LC817" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.plot_window(fig_fit, <span class="pl-s"><span class="pl-pds">&quot;</span>Inversion results: <span class="pl-pds">&quot;</span></span><span class="pl-k">+</span>f_n)</td>
      </tr>
      <tr>
        <td id="L818" class="blob-num js-line-number" data-line-number="818"></td>
        <td id="LC818" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L819" class="blob-num js-line-number" data-line-number="819"></td>
        <td id="LC819" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">plot_rtd_now</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L820" class="blob-num js-line-number" data-line-number="820"></td>
        <td id="LC820" class="blob-code blob-code-inner js-file-line">        f_n <span class="pl-k">=</span> <span class="pl-c1">self</span>.var_review.get()</td>
      </tr>
      <tr>
        <td id="L821" class="blob-num js-line-number" data-line-number="821"></td>
        <td id="LC821" class="blob-code blob-code-inner js-file-line">        fig_debye <span class="pl-k">=</span> <span class="pl-c1">self</span>.all_results[f_n][<span class="pl-s"><span class="pl-pds">&quot;</span>sol<span class="pl-pds">&quot;</span></span>].plot_rtd(<span class="pl-v">save</span><span class="pl-k">=</span><span class="pl-c1">False</span>, <span class="pl-v">draw</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L822" class="blob-num js-line-number" data-line-number="822"></td>
        <td id="LC822" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.plot_window(fig_debye, <span class="pl-s"><span class="pl-pds">&quot;</span>Debye RTD: <span class="pl-pds">&quot;</span></span><span class="pl-k">+</span>f_n)</td>
      </tr>
      <tr>
        <td id="L823" class="blob-num js-line-number" data-line-number="823"></td>
        <td id="LC823" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L824" class="blob-num js-line-number" data-line-number="824"></td>
        <td id="LC824" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>==============================================================================</span></td>
      </tr>
      <tr>
        <td id="L825" class="blob-num js-line-number" data-line-number="825"></td>
        <td id="LC825" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Importing data</span></td>
      </tr>
      <tr>
        <td id="L826" class="blob-num js-line-number" data-line-number="826"></td>
        <td id="LC826" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>==============================================================================</span></td>
      </tr>
      <tr>
        <td id="L827" class="blob-num js-line-number" data-line-number="827"></td>
        <td id="LC827" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L828" class="blob-num js-line-number" data-line-number="828"></td>
        <td id="LC828" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">make_browse_button</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L829" class="blob-num js-line-number" data-line-number="829"></td>
        <td id="LC829" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.but_browse <span class="pl-k">=</span> tk.Button(<span class="pl-c1">self</span>.frame_import, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">text</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Open file browser<span class="pl-pds">&quot;</span></span>, <span class="pl-v">bg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>gray97<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L830" class="blob-num js-line-number" data-line-number="830"></td>
        <td id="LC830" class="blob-code blob-code-inner js-file-line">                            <span class="pl-v">command</span> <span class="pl-k">=</span> <span class="pl-c1">self</span>.get_file_list, <span class="pl-v">relief</span><span class="pl-k">=</span>tk.<span class="pl-c1">GROOVE</span>)</td>
      </tr>
      <tr>
        <td id="L831" class="blob-num js-line-number" data-line-number="831"></td>
        <td id="LC831" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.but_browse.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">columnspan</span><span class="pl-k">=</span><span class="pl-c1">2</span>, <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">10</span>,<span class="pl-c1">10</span>), <span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">10</span>,<span class="pl-c1">10</span>), <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.E<span class="pl-k">+</span>tk.W)</td>
      </tr>
      <tr>
        <td id="L832" class="blob-num js-line-number" data-line-number="832"></td>
        <td id="LC832" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L833" class="blob-num js-line-number" data-line-number="833"></td>
        <td id="LC833" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">headers_input</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L834" class="blob-num js-line-number" data-line-number="834"></td>
        <td id="LC834" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.head <span class="pl-k">=</span> tk.IntVar()</td>
      </tr>
      <tr>
        <td id="L835" class="blob-num js-line-number" data-line-number="835"></td>
        <td id="LC835" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.head.set(<span class="pl-c1">self</span>.root_ini[<span class="pl-s"><span class="pl-pds">&quot;</span>Nb header lines<span class="pl-pds">&quot;</span></span>])  <span class="pl-c"><span class="pl-c">#</span> set last used value</span></td>
      </tr>
      <tr>
        <td id="L836" class="blob-num js-line-number" data-line-number="836"></td>
        <td id="LC836" class="blob-code blob-code-inner js-file-line">        tk.Label(<span class="pl-c1">self</span>.frame_import, <span class="pl-v">text</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Nb header lines:<span class="pl-pds">&quot;&quot;&quot;</span></span>, <span class="pl-v">justify</span> <span class="pl-k">=</span> tk.<span class="pl-c1">LEFT</span>).grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">columnspan</span><span class="pl-k">=</span><span class="pl-c1">1</span>,<span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W, <span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">10</span>,<span class="pl-c1">0</span>))</td>
      </tr>
      <tr>
        <td id="L837" class="blob-num js-line-number" data-line-number="837"></td>
        <td id="LC837" class="blob-code blob-code-inner js-file-line">        tk.Entry(<span class="pl-c1">self</span>.frame_import, <span class="pl-v">textvariable</span><span class="pl-k">=</span><span class="pl-c1">self</span>.head, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">12</span>).grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">columnspan</span><span class="pl-k">=</span><span class="pl-c1">1</span>,<span class="pl-v">sticky</span><span class="pl-k">=</span>tk.E<span class="pl-k">+</span>tk.W,<span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">10</span>,<span class="pl-c1">10</span>))</td>
      </tr>
      <tr>
        <td id="L838" class="blob-num js-line-number" data-line-number="838"></td>
        <td id="LC838" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L839" class="blob-num js-line-number" data-line-number="839"></td>
        <td id="LC839" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">phase_units</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L840" class="blob-num js-line-number" data-line-number="840"></td>
        <td id="LC840" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> Phase units</span></td>
      </tr>
      <tr>
        <td id="L841" class="blob-num js-line-number" data-line-number="841"></td>
        <td id="LC841" class="blob-code blob-code-inner js-file-line">        unites <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&quot;</span>mrad<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>rad<span class="pl-pds">&quot;</span></span> ,<span class="pl-s"><span class="pl-pds">&quot;</span>deg<span class="pl-pds">&quot;</span></span>]</td>
      </tr>
      <tr>
        <td id="L842" class="blob-num js-line-number" data-line-number="842"></td>
        <td id="LC842" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.units <span class="pl-k">=</span> tk.StringVar()</td>
      </tr>
      <tr>
        <td id="L843" class="blob-num js-line-number" data-line-number="843"></td>
        <td id="LC843" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.units.set(<span class="pl-c1">self</span>.root_ini[<span class="pl-s"><span class="pl-pds">&quot;</span>Phase units<span class="pl-pds">&quot;</span></span>])  <span class="pl-c"><span class="pl-c">#</span> set last used value</span></td>
      </tr>
      <tr>
        <td id="L844" class="blob-num js-line-number" data-line-number="844"></td>
        <td id="LC844" class="blob-code blob-code-inner js-file-line">        tk.Label(<span class="pl-c1">self</span>.frame_import, <span class="pl-v">text</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Phase units:<span class="pl-pds">&quot;&quot;&quot;</span></span>, <span class="pl-v">justify</span> <span class="pl-k">=</span> tk.<span class="pl-c1">LEFT</span>).grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">2</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W, <span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">10</span>,<span class="pl-c1">0</span>))</td>
      </tr>
      <tr>
        <td id="L845" class="blob-num js-line-number" data-line-number="845"></td>
        <td id="LC845" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> i, u <span class="pl-k">in</span> <span class="pl-c1">enumerate</span>(unites):</td>
      </tr>
      <tr>
        <td id="L846" class="blob-num js-line-number" data-line-number="846"></td>
        <td id="LC846" class="blob-code blob-code-inner js-file-line">            tk.Radiobutton(<span class="pl-c1">self</span>.frame_import, <span class="pl-v">text</span><span class="pl-k">=</span>u, <span class="pl-v">variable</span><span class="pl-k">=</span><span class="pl-c1">self</span>.units, <span class="pl-v">command</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-v">value</span><span class="pl-k">=</span>u).grid(<span class="pl-v">row</span><span class="pl-k">=</span>i<span class="pl-k">+</span><span class="pl-c1">2</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W, <span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">10</span>,<span class="pl-c1">10</span>), <span class="pl-v">pady</span><span class="pl-k">=</span>pad_radio)</td>
      </tr>
      <tr>
        <td id="L847" class="blob-num js-line-number" data-line-number="847"></td>
        <td id="LC847" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L848" class="blob-num js-line-number" data-line-number="848"></td>
        <td id="LC848" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">get_file_list</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L849" class="blob-num js-line-number" data-line-number="849"></td>
        <td id="LC849" class="blob-code blob-code-inner js-file-line">        files <span class="pl-k">=</span> tkinter.filedialog.askopenfilenames(<span class="pl-v">parent</span><span class="pl-k">=</span><span class="pl-c1">self</span>.master,<span class="pl-v">title</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Choose a file<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L850" class="blob-num js-line-number" data-line-number="850"></td>
        <td id="LC850" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.open_files <span class="pl-k">=</span> <span class="pl-c1">sorted</span>(<span class="pl-c1">list</span>(files))</td>
      </tr>
      <tr>
        <td id="L851" class="blob-num js-line-number" data-line-number="851"></td>
        <td id="LC851" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.draw_file_list()</td>
      </tr>
      <tr>
        <td id="L852" class="blob-num js-line-number" data-line-number="852"></td>
        <td id="LC852" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L853" class="blob-num js-line-number" data-line-number="853"></td>
        <td id="LC853" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">draw_file_list</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L854" class="blob-num js-line-number" data-line-number="854"></td>
        <td id="LC854" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L855" class="blob-num js-line-number" data-line-number="855"></td>
        <td id="LC855" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.frame_path <span class="pl-k">=</span> tk.Frame(<span class="pl-c1">self</span>.frame_list)</td>
      </tr>
      <tr>
        <td id="L856" class="blob-num js-line-number" data-line-number="856"></td>
        <td id="LC856" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.frame_path.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">padx</span><span class="pl-k">=</span><span class="pl-c1">20</span>, <span class="pl-v">pady</span><span class="pl-k">=</span><span class="pl-c1">10</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.E<span class="pl-k">+</span>tk.W)</td>
      </tr>
      <tr>
        <td id="L857" class="blob-num js-line-number" data-line-number="857"></td>
        <td id="LC857" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.frame_path.columnconfigure(<span class="pl-c1">2</span>, <span class="pl-v">weight</span><span class="pl-k">=</span><span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L858" class="blob-num js-line-number" data-line-number="858"></td>
        <td id="LC858" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L859" class="blob-num js-line-number" data-line-number="859"></td>
        <td id="LC859" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.frame_select <span class="pl-k">=</span> tk.Frame(<span class="pl-c1">self</span>.frame_list)</td>
      </tr>
      <tr>
        <td id="L860" class="blob-num js-line-number" data-line-number="860"></td>
        <td id="LC860" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.frame_select.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">20</span>,<span class="pl-c1">0</span>), <span class="pl-v">pady</span><span class="pl-k">=</span><span class="pl-c1">10</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.E<span class="pl-k">+</span>tk.W<span class="pl-k">+</span>tk.S<span class="pl-k">+</span>tk.N)</td>
      </tr>
      <tr>
        <td id="L861" class="blob-num js-line-number" data-line-number="861"></td>
        <td id="LC861" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.frame_select.columnconfigure(<span class="pl-c1">0</span>, <span class="pl-v">weight</span><span class="pl-k">=</span><span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L862" class="blob-num js-line-number" data-line-number="862"></td>
        <td id="LC862" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.frame_select.rowconfigure(<span class="pl-c1">1</span>, <span class="pl-v">weight</span><span class="pl-k">=</span><span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L863" class="blob-num js-line-number" data-line-number="863"></td>
        <td id="LC863" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L864" class="blob-num js-line-number" data-line-number="864"></td>
        <td id="LC864" class="blob-code blob-code-inner js-file-line">        text_loc <span class="pl-k">=</span> tk.Text(<span class="pl-c1">self</span>.frame_path, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">40</span>, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">3</span>, <span class="pl-v">font</span><span class="pl-k">=</span>fontz[<span class="pl-s"><span class="pl-pds">&quot;</span>normal_small<span class="pl-pds">&quot;</span></span>])</td>
      </tr>
      <tr>
        <td id="L865" class="blob-num js-line-number" data-line-number="865"></td>
        <td id="LC865" class="blob-code blob-code-inner js-file-line">        text_loc.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">rowspan</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.N<span class="pl-k">+</span>tk.W<span class="pl-k">+</span>tk.E)</td>
      </tr>
      <tr>
        <td id="L866" class="blob-num js-line-number" data-line-number="866"></td>
        <td id="LC866" class="blob-code blob-code-inner js-file-line">        s <span class="pl-k">=</span> tk.Scrollbar(<span class="pl-c1">self</span>.frame_select, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">20</span>)</td>
      </tr>
      <tr>
        <td id="L867" class="blob-num js-line-number" data-line-number="867"></td>
        <td id="LC867" class="blob-code blob-code-inner js-file-line">        s.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">2</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.E<span class="pl-k">+</span>tk.N<span class="pl-k">+</span>tk.S, <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">0</span>,<span class="pl-c1">10</span>))</td>
      </tr>
      <tr>
        <td id="L868" class="blob-num js-line-number" data-line-number="868"></td>
        <td id="LC868" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.text_files <span class="pl-k">=</span> tk.Listbox(<span class="pl-c1">self</span>.frame_select, <span class="pl-v">selectmode</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>extended<span class="pl-pds">&#39;</span></span>, <span class="pl-v">font</span><span class="pl-k">=</span>fontz[<span class="pl-s"><span class="pl-pds">&quot;</span>italic_small<span class="pl-pds">&quot;</span></span>])</td>
      </tr>
      <tr>
        <td id="L869" class="blob-num js-line-number" data-line-number="869"></td>
        <td id="LC869" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.text_files.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">columnspan</span><span class="pl-k">=</span><span class="pl-c1">2</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.S<span class="pl-k">+</span>tk.W<span class="pl-k">+</span>tk.E<span class="pl-k">+</span>tk.N, <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">0</span>,<span class="pl-c1">0</span>))</td>
      </tr>
      <tr>
        <td id="L870" class="blob-num js-line-number" data-line-number="870"></td>
        <td id="LC870" class="blob-code blob-code-inner js-file-line">        s[<span class="pl-s"><span class="pl-pds">&#39;</span>command<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-c1">self</span>.text_files.yview</td>
      </tr>
      <tr>
        <td id="L871" class="blob-num js-line-number" data-line-number="871"></td>
        <td id="LC871" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.text_files[<span class="pl-s"><span class="pl-pds">&#39;</span>yscrollcommand<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> s.set</td>
      </tr>
      <tr>
        <td id="L872" class="blob-num js-line-number" data-line-number="872"></td>
        <td id="LC872" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L873" class="blob-num js-line-number" data-line-number="873"></td>
        <td id="LC873" class="blob-code blob-code-inner js-file-line">        tk.Button(<span class="pl-c1">self</span>.frame_select, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">text</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Preview selected data files<span class="pl-pds">&quot;</span></span>, <span class="pl-v">command</span><span class="pl-k">=</span><span class="pl-c1">self</span>.preview_data, <span class="pl-v">bg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>gray97<span class="pl-pds">&#39;</span></span>, <span class="pl-v">font</span><span class="pl-k">=</span>fontz[<span class="pl-s"><span class="pl-pds">&quot;</span>normal_small<span class="pl-pds">&quot;</span></span>], <span class="pl-v">relief</span><span class="pl-k">=</span>tk.<span class="pl-c1">GROOVE</span>).grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">2</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">columnspan</span><span class="pl-k">=</span><span class="pl-c1">2</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W<span class="pl-k">+</span>tk.E)</td>
      </tr>
      <tr>
        <td id="L874" class="blob-num js-line-number" data-line-number="874"></td>
        <td id="LC874" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> Select all or none functions</span></td>
      </tr>
      <tr>
        <td id="L875" class="blob-num js-line-number" data-line-number="875"></td>
        <td id="LC875" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">def</span> <span class="pl-en">select_all</span>(): <span class="pl-c"><span class="pl-c">#</span> self expl</span></td>
      </tr>
      <tr>
        <td id="L876" class="blob-num js-line-number" data-line-number="876"></td>
        <td id="LC876" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.text_files.select_set(<span class="pl-c1">0</span>, tk.<span class="pl-c1">END</span>)</td>
      </tr>
      <tr>
        <td id="L877" class="blob-num js-line-number" data-line-number="877"></td>
        <td id="LC877" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">def</span> <span class="pl-en">select_none</span>(): <span class="pl-c"><span class="pl-c">#</span> self expl</span></td>
      </tr>
      <tr>
        <td id="L878" class="blob-num js-line-number" data-line-number="878"></td>
        <td id="LC878" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.text_files.select_clear(<span class="pl-c1">0</span>, tk.<span class="pl-c1">END</span>)</td>
      </tr>
      <tr>
        <td id="L879" class="blob-num js-line-number" data-line-number="879"></td>
        <td id="LC879" class="blob-code blob-code-inner js-file-line">        tk.Button(<span class="pl-c1">self</span>.frame_select, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">15</span>, <span class="pl-v">text</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Select all<span class="pl-pds">&quot;</span></span>, <span class="pl-v">command</span><span class="pl-k">=</span>select_all, <span class="pl-v">bg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>gray97<span class="pl-pds">&#39;</span></span>, <span class="pl-v">font</span><span class="pl-k">=</span>fontz[<span class="pl-s"><span class="pl-pds">&quot;</span>normal_small<span class="pl-pds">&quot;</span></span>], <span class="pl-v">relief</span><span class="pl-k">=</span>tk.<span class="pl-c1">GROOVE</span>).grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.W<span class="pl-k">+</span>tk.N, <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">0</span>,<span class="pl-c1">0</span>))</td>
      </tr>
      <tr>
        <td id="L880" class="blob-num js-line-number" data-line-number="880"></td>
        <td id="LC880" class="blob-code blob-code-inner js-file-line">        tk.Button(<span class="pl-c1">self</span>.frame_select, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">15</span>, <span class="pl-v">text</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Select none<span class="pl-pds">&quot;</span></span>, <span class="pl-v">command</span><span class="pl-k">=</span>select_none, <span class="pl-v">bg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>gray97<span class="pl-pds">&#39;</span></span>, <span class="pl-v">font</span><span class="pl-k">=</span>fontz[<span class="pl-s"><span class="pl-pds">&quot;</span>normal_small<span class="pl-pds">&quot;</span></span>], <span class="pl-v">relief</span><span class="pl-k">=</span>tk.<span class="pl-c1">GROOVE</span>).grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.E<span class="pl-k">+</span>tk.N, <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">0</span>,<span class="pl-c1">0</span>))</td>
      </tr>
      <tr>
        <td id="L881" class="blob-num js-line-number" data-line-number="881"></td>
        <td id="LC881" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L882" class="blob-num js-line-number" data-line-number="882"></td>
        <td id="LC882" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> Fill list box</span></td>
      </tr>
      <tr>
        <td id="L883" class="blob-num js-line-number" data-line-number="883"></td>
        <td id="LC883" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">len</span>(<span class="pl-c1">self</span>.open_files) <span class="pl-k">&gt;=</span> <span class="pl-c1">1</span>: <span class="pl-c"><span class="pl-c">#</span> Only draw this listbox if files were selected in browser</span></td>
      </tr>
      <tr>
        <td id="L884" class="blob-num js-line-number" data-line-number="884"></td>
        <td id="LC884" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> (i, o) <span class="pl-k">in</span> <span class="pl-c1">enumerate</span>(<span class="pl-c1">self</span>.open_files):</td>
      </tr>
      <tr>
        <td id="L885" class="blob-num js-line-number" data-line-number="885"></td>
        <td id="LC885" class="blob-code blob-code-inner js-file-line">                fil <span class="pl-k">=</span> o.split(<span class="pl-s"><span class="pl-pds">&quot;</span>/<span class="pl-pds">&quot;</span></span>)[<span class="pl-k">-</span><span class="pl-c1">1</span>] <span class="pl-c"><span class="pl-c">#</span> Split full path to keep only name and extension</span></td>
      </tr>
      <tr>
        <td id="L886" class="blob-num js-line-number" data-line-number="886"></td>
        <td id="LC886" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.text_files.insert(i, fil) <span class="pl-c"><span class="pl-c">#</span> Insert items 1 by 1 in loop</span></td>
      </tr>
      <tr>
        <td id="L887" class="blob-num js-line-number" data-line-number="887"></td>
        <td id="LC887" class="blob-code blob-code-inner js-file-line">            locs <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>/<span class="pl-pds">&quot;</span></span>.join(<span class="pl-c1">self</span>.open_files[<span class="pl-c1">0</span>].split(<span class="pl-s"><span class="pl-pds">&quot;</span>/<span class="pl-pds">&quot;</span></span>)[:<span class="pl-k">-</span><span class="pl-c1">1</span>])<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span>/<span class="pl-pds">&quot;</span></span> <span class="pl-c"><span class="pl-c">#</span> Path to imported files in string format</span></td>
      </tr>
      <tr>
        <td id="L888" class="blob-num js-line-number" data-line-number="888"></td>
        <td id="LC888" class="blob-code blob-code-inner js-file-line">            text_loc.insert(<span class="pl-s"><span class="pl-pds">&quot;</span>1.0<span class="pl-pds">&quot;</span></span>, locs) <span class="pl-c"><span class="pl-c">#</span> Insert path to empty text box</span></td>
      </tr>
      <tr>
        <td id="L889" class="blob-num js-line-number" data-line-number="889"></td>
        <td id="LC889" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.text_files.select_set(<span class="pl-c1">0</span>) <span class="pl-c"><span class="pl-c">#</span> Select first item in list after populating</span></td>
      </tr>
      <tr>
        <td id="L890" class="blob-num js-line-number" data-line-number="890"></td>
        <td id="LC890" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L891" class="blob-num js-line-number" data-line-number="891"></td>
        <td id="LC891" class="blob-code blob-code-inner js-file-line">            text_loc.insert(<span class="pl-s"><span class="pl-pds">&quot;</span>1.0<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>None imported<span class="pl-pds">&quot;</span></span>) <span class="pl-c"><span class="pl-c">#</span> Empty list box if no files selected</span></td>
      </tr>
      <tr>
        <td id="L892" class="blob-num js-line-number" data-line-number="892"></td>
        <td id="LC892" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L893" class="blob-num js-line-number" data-line-number="893"></td>
        <td id="LC893" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>==============================================================================</span></td>
      </tr>
      <tr>
        <td id="L894" class="blob-num js-line-number" data-line-number="894"></td>
        <td id="LC894" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Save and load GUI state</span></td>
      </tr>
      <tr>
        <td id="L895" class="blob-num js-line-number" data-line-number="895"></td>
        <td id="LC895" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>==============================================================================</span></td>
      </tr>
      <tr>
        <td id="L896" class="blob-num js-line-number" data-line-number="896"></td>
        <td id="LC896" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L897" class="blob-num js-line-number" data-line-number="897"></td>
        <td id="LC897" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">load</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L898" class="blob-num js-line-number" data-line-number="898"></td>
        <td id="LC898" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\n</span>Loading root_ini from:<span class="pl-cce">\n</span><span class="pl-pds">&quot;</span></span>, <span class="pl-c1">self</span>.working_path)</td>
      </tr>
      <tr>
        <td id="L899" class="blob-num js-line-number" data-line-number="899"></td>
        <td id="LC899" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L900" class="blob-num js-line-number" data-line-number="900"></td>
        <td id="LC900" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">with</span> <span class="pl-c1">open</span>(<span class="pl-c1">self</span>.working_path<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&#39;</span>root_ini<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> f:</td>
      </tr>
      <tr>
        <td id="L901" class="blob-num js-line-number" data-line-number="901"></td>
        <td id="LC901" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.root_ini <span class="pl-k">=</span> jload(f)</td>
      </tr>
      <tr>
        <td id="L902" class="blob-num js-line-number" data-line-number="902"></td>
        <td id="LC902" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>root_ini successfully loaded<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L903" class="blob-num js-line-number" data-line-number="903"></td>
        <td id="LC903" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L904" class="blob-num js-line-number" data-line-number="904"></td>
        <td id="LC904" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>root_ini not found, using default values<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L905" class="blob-num js-line-number" data-line-number="905"></td>
        <td id="LC905" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.root_ini <span class="pl-k">=</span> <span class="pl-c1">self</span>.use_default_root_ini()</td>
      </tr>
      <tr>
        <td id="L906" class="blob-num js-line-number" data-line-number="906"></td>
        <td id="LC906" class="blob-code blob-code-inner js-file-line">        stdout.flush()</td>
      </tr>
      <tr>
        <td id="L907" class="blob-num js-line-number" data-line-number="907"></td>
        <td id="LC907" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L908" class="blob-num js-line-number" data-line-number="908"></td>
        <td id="LC908" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">save</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L909" class="blob-num js-line-number" data-line-number="909"></td>
        <td id="LC909" class="blob-code blob-code-inner js-file-line">        root_save <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L910" class="blob-num js-line-number" data-line-number="910"></td>
        <td id="LC910" class="blob-code blob-code-inner js-file-line">                        <span class="pl-s"><span class="pl-pds">&quot;</span>Spectral IP model<span class="pl-pds">&quot;</span></span>     : <span class="pl-c1">self</span>.model.get(),</td>
      </tr>
      <tr>
        <td id="L911" class="blob-num js-line-number" data-line-number="911"></td>
        <td id="LC911" class="blob-code blob-code-inner js-file-line">                        <span class="pl-s"><span class="pl-pds">&quot;</span>Adaptive Metropolis<span class="pl-pds">&quot;</span></span>   : <span class="pl-c1">self</span>.adaptive.get(),</td>
      </tr>
      <tr>
        <td id="L912" class="blob-num js-line-number" data-line-number="912"></td>
        <td id="LC912" class="blob-code blob-code-inner js-file-line">                        <span class="pl-s"><span class="pl-pds">&quot;</span>Nb header lines<span class="pl-pds">&quot;</span></span>       : <span class="pl-c1">self</span>.head.get(),</td>
      </tr>
      <tr>
        <td id="L913" class="blob-num js-line-number" data-line-number="913"></td>
        <td id="LC913" class="blob-code blob-code-inner js-file-line">                        <span class="pl-s"><span class="pl-pds">&quot;</span>Phase units<span class="pl-pds">&quot;</span></span>           : <span class="pl-c1">self</span>.units.get(),</td>
      </tr>
      <tr>
        <td id="L914" class="blob-num js-line-number" data-line-number="914"></td>
        <td id="LC914" class="blob-code blob-code-inner js-file-line">                        <span class="pl-s"><span class="pl-pds">&quot;</span>Imported files<span class="pl-pds">&quot;</span></span>        : <span class="pl-c1">self</span>.open_files,</td>
      </tr>
      <tr>
        <td id="L915" class="blob-num js-line-number" data-line-number="915"></td>
        <td id="LC915" class="blob-code blob-code-inner js-file-line">                        <span class="pl-s"><span class="pl-pds">&quot;</span>Polyn order<span class="pl-pds">&quot;</span></span>           : <span class="pl-c1">self</span>.poly_n.get(),</td>
      </tr>
      <tr>
        <td id="L916" class="blob-num js-line-number" data-line-number="916"></td>
        <td id="LC916" class="blob-code blob-code-inner js-file-line">                        <span class="pl-s"><span class="pl-pds">&quot;</span>Freq dep<span class="pl-pds">&quot;</span></span>              : <span class="pl-c1">self</span>.c_exp.get(),</td>
      </tr>
      <tr>
        <td id="L917" class="blob-num js-line-number" data-line-number="917"></td>
        <td id="LC917" class="blob-code blob-code-inner js-file-line">                        <span class="pl-s"><span class="pl-pds">&quot;</span>Nb modes<span class="pl-pds">&quot;</span></span>              : <span class="pl-c1">self</span>.modes_n.get(),</td>
      </tr>
      <tr>
        <td id="L918" class="blob-num js-line-number" data-line-number="918"></td>
        <td id="LC918" class="blob-code blob-code-inner js-file-line">                        <span class="pl-s"><span class="pl-pds">&quot;</span>Lambda<span class="pl-pds">&quot;</span></span>                : <span class="pl-c1">self</span>.lamb_da.get(),</td>
      </tr>
      <tr>
        <td id="L919" class="blob-num js-line-number" data-line-number="919"></td>
        <td id="LC919" class="blob-code blob-code-inner js-file-line">                    }</td>
      </tr>
      <tr>
        <td id="L920" class="blob-num js-line-number" data-line-number="920"></td>
        <td id="LC920" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L921" class="blob-num js-line-number" data-line-number="921"></td>
        <td id="LC921" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> k, v <span class="pl-k">in</span> <span class="pl-c1">list</span>(<span class="pl-c1">self</span>.mcmc_vars.items()):</td>
      </tr>
      <tr>
        <td id="L922" class="blob-num js-line-number" data-line-number="922"></td>
        <td id="LC922" class="blob-code blob-code-inner js-file-line">            root_save[k] <span class="pl-k">=</span> v[<span class="pl-c1">0</span>].get()</td>
      </tr>
      <tr>
        <td id="L923" class="blob-num js-line-number" data-line-number="923"></td>
        <td id="LC923" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> k, v <span class="pl-k">in</span> <span class="pl-c1">list</span>(<span class="pl-c1">self</span>.save_options.items()):</td>
      </tr>
      <tr>
        <td id="L924" class="blob-num js-line-number" data-line-number="924"></td>
        <td id="LC924" class="blob-code blob-code-inner js-file-line">            root_save[k] <span class="pl-k">=</span> v.get()</td>
      </tr>
      <tr>
        <td id="L925" class="blob-num js-line-number" data-line-number="925"></td>
        <td id="LC925" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> k, v <span class="pl-k">in</span> <span class="pl-c1">list</span>(<span class="pl-c1">self</span>.run_options.items()):</td>
      </tr>
      <tr>
        <td id="L926" class="blob-num js-line-number" data-line-number="926"></td>
        <td id="LC926" class="blob-code blob-code-inner js-file-line">            root_save[k] <span class="pl-k">=</span> v.get()</td>
      </tr>
      <tr>
        <td id="L927" class="blob-num js-line-number" data-line-number="927"></td>
        <td id="LC927" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L928" class="blob-num js-line-number" data-line-number="928"></td>
        <td id="LC928" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\n</span>Saving root_ini<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L929" class="blob-num js-line-number" data-line-number="929"></td>
        <td id="LC929" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">with</span> <span class="pl-c1">open</span>(<span class="pl-c1">self</span>.working_path<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&#39;</span>root_ini<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>w<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> f:</td>
      </tr>
      <tr>
        <td id="L930" class="blob-num js-line-number" data-line-number="930"></td>
        <td id="LC930" class="blob-code blob-code-inner js-file-line">            jdump(root_save, f)</td>
      </tr>
      <tr>
        <td id="L931" class="blob-num js-line-number" data-line-number="931"></td>
        <td id="LC931" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>root_ini successfully saved in:<span class="pl-cce">\n</span><span class="pl-pds">&quot;</span></span>, <span class="pl-c1">self</span>.working_path)</td>
      </tr>
      <tr>
        <td id="L932" class="blob-num js-line-number" data-line-number="932"></td>
        <td id="LC932" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\n</span>=========END=========<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L933" class="blob-num js-line-number" data-line-number="933"></td>
        <td id="LC933" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L934" class="blob-num js-line-number" data-line-number="934"></td>
        <td id="LC934" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>==============================================================================</span></td>
      </tr>
      <tr>
        <td id="L935" class="blob-num js-line-number" data-line-number="935"></td>
        <td id="LC935" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Build menubar File, Help</span></td>
      </tr>
      <tr>
        <td id="L936" class="blob-num js-line-number" data-line-number="936"></td>
        <td id="LC936" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>==============================================================================</span></td>
      </tr>
      <tr>
        <td id="L937" class="blob-num js-line-number" data-line-number="937"></td>
        <td id="LC937" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">build_helpmenu</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L938" class="blob-num js-line-number" data-line-number="938"></td>
        <td id="LC938" class="blob-code blob-code-inner js-file-line">        menubar <span class="pl-k">=</span> tk.Menu(<span class="pl-c1">self</span>.master)</td>
      </tr>
      <tr>
        <td id="L939" class="blob-num js-line-number" data-line-number="939"></td>
        <td id="LC939" class="blob-code blob-code-inner js-file-line">        filemenu <span class="pl-k">=</span> tk.Menu(menubar, <span class="pl-v">tearoff</span><span class="pl-k">=</span><span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L940" class="blob-num js-line-number" data-line-number="940"></td>
        <td id="LC940" class="blob-code blob-code-inner js-file-line">        helpmenu <span class="pl-k">=</span> tk.Menu(menubar, <span class="pl-v">tearoff</span><span class="pl-k">=</span><span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L941" class="blob-num js-line-number" data-line-number="941"></td>
        <td id="LC941" class="blob-code blob-code-inner js-file-line">        filemenu.add_command(<span class="pl-v">label</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Open<span class="pl-pds">&quot;</span></span>, <span class="pl-v">command</span><span class="pl-k">=</span><span class="pl-c1">self</span>.get_file_list)</td>
      </tr>
      <tr>
        <td id="L942" class="blob-num js-line-number" data-line-number="942"></td>
        <td id="LC942" class="blob-code blob-code-inner js-file-line">        filemenu.add_separator()</td>
      </tr>
      <tr>
        <td id="L943" class="blob-num js-line-number" data-line-number="943"></td>
        <td id="LC943" class="blob-code blob-code-inner js-file-line">        filemenu.add_command(<span class="pl-v">label</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Exit<span class="pl-pds">&quot;</span></span>, <span class="pl-v">command</span><span class="pl-k">=</span><span class="pl-c1">self</span>.master.destroy)</td>
      </tr>
      <tr>
        <td id="L944" class="blob-num js-line-number" data-line-number="944"></td>
        <td id="LC944" class="blob-code blob-code-inner js-file-line">        menubar.add_cascade(<span class="pl-v">label</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>File<span class="pl-pds">&quot;</span></span>, <span class="pl-v">menu</span><span class="pl-k">=</span>filemenu)</td>
      </tr>
      <tr>
        <td id="L945" class="blob-num js-line-number" data-line-number="945"></td>
        <td id="LC945" class="blob-code blob-code-inner js-file-line">        helpmenu.add_command(<span class="pl-v">label</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Data file template<span class="pl-pds">&quot;</span></span>, <span class="pl-v">command</span><span class="pl-k">=</span><span class="pl-k">lambda</span>: TextMessage().popup(<span class="pl-s"><span class="pl-pds">&quot;</span>Data file template<span class="pl-pds">&quot;</span></span>, TextMessage.data_template, <span class="pl-v">size</span><span class="pl-k">=</span>fontsize))</td>
      </tr>
      <tr>
        <td id="L946" class="blob-num js-line-number" data-line-number="946"></td>
        <td id="LC946" class="blob-code blob-code-inner js-file-line">        helpmenu.add_command(<span class="pl-v">label</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>MCMC parameters<span class="pl-pds">&quot;</span></span>, <span class="pl-v">command</span><span class="pl-k">=</span><span class="pl-k">lambda</span>: TextMessage().popup(<span class="pl-s"><span class="pl-pds">&quot;</span>Markov-chain Monte Carlo parameters<span class="pl-pds">&quot;</span></span>, TextMessage.mcmc_info, <span class="pl-v">size</span><span class="pl-k">=</span>fontsize))</td>
      </tr>
      <tr>
        <td id="L947" class="blob-num js-line-number" data-line-number="947"></td>
        <td id="LC947" class="blob-code blob-code-inner js-file-line">        helpmenu.add_command(<span class="pl-v">label</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>References<span class="pl-pds">&quot;</span></span>, <span class="pl-v">command</span><span class="pl-k">=</span><span class="pl-k">lambda</span>: TextMessage().popup(<span class="pl-s"><span class="pl-pds">&quot;</span>References<span class="pl-pds">&quot;</span></span>, TextMessage.references, <span class="pl-v">size</span><span class="pl-k">=</span>fontsize))</td>
      </tr>
      <tr>
        <td id="L948" class="blob-num js-line-number" data-line-number="948"></td>
        <td id="LC948" class="blob-code blob-code-inner js-file-line">        helpmenu.add_separator()</td>
      </tr>
      <tr>
        <td id="L949" class="blob-num js-line-number" data-line-number="949"></td>
        <td id="LC949" class="blob-code blob-code-inner js-file-line">        helpmenu.add_command(<span class="pl-v">label</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>License<span class="pl-pds">&quot;</span></span>, <span class="pl-v">command</span><span class="pl-k">=</span><span class="pl-k">lambda</span>: TextMessage().popup(<span class="pl-s"><span class="pl-pds">&quot;</span>License information<span class="pl-pds">&quot;</span></span>, TextMessage.license_info, <span class="pl-v">size</span><span class="pl-k">=</span>fontsize))</td>
      </tr>
      <tr>
        <td id="L950" class="blob-num js-line-number" data-line-number="950"></td>
        <td id="LC950" class="blob-code blob-code-inner js-file-line">        helpmenu.add_command(<span class="pl-v">label</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>About<span class="pl-pds">&quot;</span></span>, <span class="pl-v">command</span><span class="pl-k">=</span><span class="pl-k">lambda</span> : TextMessage().about(fontz))</td>
      </tr>
      <tr>
        <td id="L951" class="blob-num js-line-number" data-line-number="951"></td>
        <td id="LC951" class="blob-code blob-code-inner js-file-line">        menubar.add_cascade(<span class="pl-v">label</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Help<span class="pl-pds">&quot;</span></span>, <span class="pl-v">menu</span><span class="pl-k">=</span>helpmenu)</td>
      </tr>
      <tr>
        <td id="L952" class="blob-num js-line-number" data-line-number="952"></td>
        <td id="LC952" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.master.config(<span class="pl-v">menu</span><span class="pl-k">=</span>menubar)</td>
      </tr>
      <tr>
        <td id="L953" class="blob-num js-line-number" data-line-number="953"></td>
        <td id="LC953" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L954" class="blob-num js-line-number" data-line-number="954"></td>
        <td id="LC954" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L955" class="blob-num js-line-number" data-line-number="955"></td>
        <td id="LC955" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L956" class="blob-num js-line-number" data-line-number="956"></td>
        <td id="LC956" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>==============================================================================</span></td>
      </tr>
      <tr>
        <td id="L957" class="blob-num js-line-number" data-line-number="957"></td>
        <td id="LC957" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Class for popup messages</span></td>
      </tr>
      <tr>
        <td id="L958" class="blob-num js-line-number" data-line-number="958"></td>
        <td id="LC958" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>==============================================================================</span></td>
      </tr>
      <tr>
        <td id="L959" class="blob-num js-line-number" data-line-number="959"></td>
        <td id="LC959" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">TextMessage</span>(<span class="pl-c1">object</span>):</td>
      </tr>
      <tr>
        <td id="L960" class="blob-num js-line-number" data-line-number="960"></td>
        <td id="LC960" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L961" class="blob-num js-line-number" data-line-number="961"></td>
        <td id="LC961" class="blob-code blob-code-inner js-file-line">    data_template <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>DATA FILE TEMPLATE</span></td>
      </tr>
      <tr>
        <td id="L962" class="blob-num js-line-number" data-line-number="962"></td>
        <td id="LC962" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L963" class="blob-num js-line-number" data-line-number="963"></td>
        <td id="LC963" class="blob-code blob-code-inner js-file-line"><span class="pl-s">Save data in .csv, .txt, .dat, ... extension file</span></td>
      </tr>
      <tr>
        <td id="L964" class="blob-num js-line-number" data-line-number="964"></td>
        <td id="LC964" class="blob-code blob-code-inner js-file-line"><span class="pl-s">Comma separation between columns is mandatory</span></td>
      </tr>
      <tr>
        <td id="L965" class="blob-num js-line-number" data-line-number="965"></td>
        <td id="LC965" class="blob-code blob-code-inner js-file-line"><span class="pl-s">Column order is very important</span></td>
      </tr>
      <tr>
        <td id="L966" class="blob-num js-line-number" data-line-number="966"></td>
        <td id="LC966" class="blob-code blob-code-inner js-file-line"><span class="pl-s">Phase units may be milliradians, radians or degrees</span></td>
      </tr>
      <tr>
        <td id="L967" class="blob-num js-line-number" data-line-number="967"></td>
        <td id="LC967" class="blob-code blob-code-inner js-file-line"><span class="pl-s">Units are specified in main window</span></td>
      </tr>
      <tr>
        <td id="L968" class="blob-num js-line-number" data-line-number="968"></td>
        <td id="LC968" class="blob-code blob-code-inner js-file-line"><span class="pl-s">Amplitude units may be Ohm-m or Ohm</span></td>
      </tr>
      <tr>
        <td id="L969" class="blob-num js-line-number" data-line-number="969"></td>
        <td id="LC969" class="blob-code blob-code-inner js-file-line"><span class="pl-s">A number of header lines may be skipped in the main window</span></td>
      </tr>
      <tr>
        <td id="L970" class="blob-num js-line-number" data-line-number="970"></td>
        <td id="LC970" class="blob-code blob-code-inner js-file-line"><span class="pl-s">In this example Nb header lines = 1</span></td>
      </tr>
      <tr>
        <td id="L971" class="blob-num js-line-number" data-line-number="971"></td>
        <td id="LC971" class="blob-code blob-code-inner js-file-line"><span class="pl-s">To skip high-frequencies, increase Nb header lines</span></td>
      </tr>
      <tr>
        <td id="L972" class="blob-num js-line-number" data-line-number="972"></td>
        <td id="LC972" class="blob-code blob-code-inner js-file-line"><span class="pl-s">Scientific or standard notation is OK</span></td>
      </tr>
      <tr>
        <td id="L973" class="blob-num js-line-number" data-line-number="973"></td>
        <td id="LC973" class="blob-code blob-code-inner js-file-line"><span class="pl-s">Data must be formatted using the following template:</span></td>
      </tr>
      <tr>
        <td id="L974" class="blob-num js-line-number" data-line-number="974"></td>
        <td id="LC974" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L975" class="blob-num js-line-number" data-line-number="975"></td>
        <td id="LC975" class="blob-code blob-code-inner js-file-line"><span class="pl-s">===============================================================================</span></td>
      </tr>
      <tr>
        <td id="L976" class="blob-num js-line-number" data-line-number="976"></td>
        <td id="LC976" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L977" class="blob-num js-line-number" data-line-number="977"></td>
        <td id="LC977" class="blob-code blob-code-inner js-file-line"><span class="pl-s">Freq (Hz), Res (Ohm-m),  Phase (deg), dRes (Ohm-m), dPhase (deg)</span></td>
      </tr>
      <tr>
        <td id="L978" class="blob-num js-line-number" data-line-number="978"></td>
        <td id="LC978" class="blob-code blob-code-inner js-file-line"><span class="pl-s">6.000e+03, 1.17152e+05, -2.36226e+02, 1.171527e+01, 9.948376e-02</span></td>
      </tr>
      <tr>
        <td id="L979" class="blob-num js-line-number" data-line-number="979"></td>
        <td id="LC979" class="blob-code blob-code-inner js-file-line"><span class="pl-s">3.000e+03, 1.22177e+05, -1.46221e+02, 1.392825e+01, 1.134464e-01</span></td>
      </tr>
      <tr>
        <td id="L980" class="blob-num js-line-number" data-line-number="980"></td>
        <td id="LC980" class="blob-code blob-code-inner js-file-line"><span class="pl-s">1.500e+03, 1.25553e+05, -9.51099e+01, 2.762214e+01, 2.199114e-01</span></td>
      </tr>
      <tr>
        <td id="L981" class="blob-num js-line-number" data-line-number="981"></td>
        <td id="LC981" class="blob-code blob-code-inner js-file-line"><span class="pl-s">........., ..........., ............, ............, ............</span></td>
      </tr>
      <tr>
        <td id="L982" class="blob-num js-line-number" data-line-number="982"></td>
        <td id="LC982" class="blob-code blob-code-inner js-file-line"><span class="pl-s">........., ..........., ............, ............, ............</span></td>
      </tr>
      <tr>
        <td id="L983" class="blob-num js-line-number" data-line-number="983"></td>
        <td id="LC983" class="blob-code blob-code-inner js-file-line"><span class="pl-s">........., ..........., ............, ............, ............</span></td>
      </tr>
      <tr>
        <td id="L984" class="blob-num js-line-number" data-line-number="984"></td>
        <td id="LC984" class="blob-code blob-code-inner js-file-line"><span class="pl-s">4.575e-02, 1.66153e+05, -1.21143e+01, 1.947314e+02, 1.171115e+00</span></td>
      </tr>
      <tr>
        <td id="L985" class="blob-num js-line-number" data-line-number="985"></td>
        <td id="LC985" class="blob-code blob-code-inner js-file-line"><span class="pl-s">2.288e-02, 1.67988e+05, -9.36718e+00, 3.306003e+02, 1.9669860+00</span></td>
      </tr>
      <tr>
        <td id="L986" class="blob-num js-line-number" data-line-number="986"></td>
        <td id="LC986" class="blob-code blob-code-inner js-file-line"><span class="pl-s">1.144e-02, 1.70107e+05, -7.25533e+00, 5.630541e+02, 3.310889e+00</span></td>
      </tr>
      <tr>
        <td id="L987" class="blob-num js-line-number" data-line-number="987"></td>
        <td id="LC987" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L988" class="blob-num js-line-number" data-line-number="988"></td>
        <td id="LC988" class="blob-code blob-code-inner js-file-line"><span class="pl-s">===============================================================================</span></td>
      </tr>
      <tr>
        <td id="L989" class="blob-num js-line-number" data-line-number="989"></td>
        <td id="LC989" class="blob-code blob-code-inner js-file-line"><span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L990" class="blob-num js-line-number" data-line-number="990"></td>
        <td id="LC990" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L991" class="blob-num js-line-number" data-line-number="991"></td>
        <td id="LC991" class="blob-code blob-code-inner js-file-line">    mcmc_info <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>===================================================================================</span></td>
      </tr>
      <tr>
        <td id="L992" class="blob-num js-line-number" data-line-number="992"></td>
        <td id="LC992" class="blob-code blob-code-inner js-file-line"><span class="pl-s">Meaning of MCMC parameters:</span></td>
      </tr>
      <tr>
        <td id="L993" class="blob-num js-line-number" data-line-number="993"></td>
        <td id="LC993" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L994" class="blob-num js-line-number" data-line-number="994"></td>
        <td id="LC994" class="blob-code blob-code-inner js-file-line"><span class="pl-s">|---------------------------# Iterations------------------------------------| = 100</span></td>
      </tr>
      <tr>
        <td id="L995" class="blob-num js-line-number" data-line-number="995"></td>
        <td id="LC995" class="blob-code blob-code-inner js-file-line"><span class="pl-s">|........Burn-in period (discarded iterations)........|---------------------| =  79</span></td>
      </tr>
      <tr>
        <td id="L996" class="blob-num js-line-number" data-line-number="996"></td>
        <td id="LC996" class="blob-code blob-code-inner js-file-line"><span class="pl-s">         Remaining iterations:                        |---------------------| =  21</span></td>
      </tr>
      <tr>
        <td id="L997" class="blob-num js-line-number" data-line-number="997"></td>
        <td id="LC997" class="blob-code blob-code-inner js-file-line"><span class="pl-s">         Thinning factor (Discard more chains):       |-..-..-..-..-..-..-..| =   3</span></td>
      </tr>
      <tr>
        <td id="L998" class="blob-num js-line-number" data-line-number="998"></td>
        <td id="LC998" class="blob-code blob-code-inner js-file-line"><span class="pl-s">         Iterations kept for histogram:                             |-------| =   7</span></td>
      </tr>
      <tr>
        <td id="L999" class="blob-num js-line-number" data-line-number="999"></td>
        <td id="LC999" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L1000" class="blob-num js-line-number" data-line-number="1000"></td>
        <td id="LC1000" class="blob-code blob-code-inner js-file-line"><span class="pl-s">         Tuning interval = 1000: the proposal scale is tuned every 1000 iteration</span></td>
      </tr>
      <tr>
        <td id="L1001" class="blob-num js-line-number" data-line-number="1001"></td>
        <td id="LC1001" class="blob-code blob-code-inner js-file-line"><span class="pl-s">         Proposal scale: the proposal distribution std = scale*parameter_value</span></td>
      </tr>
      <tr>
        <td id="L1002" class="blob-num js-line-number" data-line-number="1002"></td>
        <td id="LC1002" class="blob-code blob-code-inner js-file-line"><span class="pl-s">         Adding more chains may help sample the posterior distribution</span></td>
      </tr>
      <tr>
        <td id="L1003" class="blob-num js-line-number" data-line-number="1003"></td>
        <td id="LC1003" class="blob-code blob-code-inner js-file-line"><span class="pl-s">         More iterations will lead to better fit up until a certain point</span></td>
      </tr>
      <tr>
        <td id="L1004" class="blob-num js-line-number" data-line-number="1004"></td>
        <td id="LC1004" class="blob-code blob-code-inner js-file-line"><span class="pl-s">         Burn-in to discard the random hypotheses before convergence</span></td>
      </tr>
      <tr>
        <td id="L1005" class="blob-num js-line-number" data-line-number="1005"></td>
        <td id="LC1005" class="blob-code blob-code-inner js-file-line"><span class="pl-s">         Burn-in period is used for tuning</span></td>
      </tr>
      <tr>
        <td id="L1006" class="blob-num js-line-number" data-line-number="1006"></td>
        <td id="LC1006" class="blob-code blob-code-inner js-file-line"><span class="pl-s">         Thinning factor has no advantage for convergence or quality of fit</span></td>
      </tr>
      <tr>
        <td id="L1007" class="blob-num js-line-number" data-line-number="1007"></td>
        <td id="LC1007" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L1008" class="blob-num js-line-number" data-line-number="1008"></td>
        <td id="LC1008" class="blob-code blob-code-inner js-file-line"><span class="pl-s">         Burn-in for 90<span class="pl-c1">% o</span>f iterations</span></td>
      </tr>
      <tr>
        <td id="L1009" class="blob-num js-line-number" data-line-number="1009"></td>
        <td id="LC1009" class="blob-code blob-code-inner js-file-line"><span class="pl-s">         Use thinning factor to keep ~1000-10000 samples in histograms</span></td>
      </tr>
      <tr>
        <td id="L1010" class="blob-num js-line-number" data-line-number="1010"></td>
        <td id="LC1010" class="blob-code blob-code-inner js-file-line"><span class="pl-s">         (easier on memory)</span></td>
      </tr>
      <tr>
        <td id="L1011" class="blob-num js-line-number" data-line-number="1011"></td>
        <td id="LC1011" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L1012" class="blob-num js-line-number" data-line-number="1012"></td>
        <td id="LC1012" class="blob-code blob-code-inner js-file-line"><span class="pl-s">===================================================================================</span></td>
      </tr>
      <tr>
        <td id="L1013" class="blob-num js-line-number" data-line-number="1013"></td>
        <td id="LC1013" class="blob-code blob-code-inner js-file-line"><span class="pl-s">Recommended for data files with ~20 frequencies:</span></td>
      </tr>
      <tr>
        <td id="L1014" class="blob-num js-line-number" data-line-number="1014"></td>
        <td id="LC1014" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L1015" class="blob-num js-line-number" data-line-number="1015"></td>
        <td id="LC1015" class="blob-code blob-code-inner js-file-line"><span class="pl-s">Cole-Cole model:    Good convergence for 1 or 2 modes</span></td>
      </tr>
      <tr>
        <td id="L1016" class="blob-num js-line-number" data-line-number="1016"></td>
        <td id="LC1016" class="blob-code blob-code-inner js-file-line"><span class="pl-s">                    Slow convergence for 3 modes</span></td>
      </tr>
      <tr>
        <td id="L1017" class="blob-num js-line-number" data-line-number="1017"></td>
        <td id="LC1017" class="blob-code blob-code-inner js-file-line"><span class="pl-s">                    10 000 - 100 000 iterations for 2 modes</span></td>
      </tr>
      <tr>
        <td id="L1018" class="blob-num js-line-number" data-line-number="1018"></td>
        <td id="LC1018" class="blob-code blob-code-inner js-file-line"><span class="pl-s">                    May take &gt; 500 000 for 3 modes</span></td>
      </tr>
      <tr>
        <td id="L1019" class="blob-num js-line-number" data-line-number="1019"></td>
        <td id="LC1019" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L1020" class="blob-num js-line-number" data-line-number="1020"></td>
        <td id="LC1020" class="blob-code blob-code-inner js-file-line"><span class="pl-s">Debye model:        Good convergence for 3rd order polynomial</span></td>
      </tr>
      <tr>
        <td id="L1021" class="blob-num js-line-number" data-line-number="1021"></td>
        <td id="LC1021" class="blob-code blob-code-inner js-file-line"><span class="pl-s">                    100 000 iterations usually converges for 3rd order</span></td>
      </tr>
      <tr>
        <td id="L1022" class="blob-num js-line-number" data-line-number="1022"></td>
        <td id="LC1022" class="blob-code blob-code-inner js-file-line"><span class="pl-s">                    &gt; 100 000 iterations for 4th order polynomial</span></td>
      </tr>
      <tr>
        <td id="L1023" class="blob-num js-line-number" data-line-number="1023"></td>
        <td id="LC1023" class="blob-code blob-code-inner js-file-line"><span class="pl-s">                    Slow convergence, sometimes no convergence for 5th order</span></td>
      </tr>
      <tr>
        <td id="L1024" class="blob-num js-line-number" data-line-number="1024"></td>
        <td id="LC1024" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L1025" class="blob-num js-line-number" data-line-number="1025"></td>
        <td id="LC1025" class="blob-code blob-code-inner js-file-line"><span class="pl-s">Shin model:         10 000 - 100 000 iterations usually converges</span></td>
      </tr>
      <tr>
        <td id="L1026" class="blob-num js-line-number" data-line-number="1026"></td>
        <td id="LC1026" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L1027" class="blob-num js-line-number" data-line-number="1027"></td>
        <td id="LC1027" class="blob-code blob-code-inner js-file-line"><span class="pl-s">Dias model:         Fast convergence, weak fits</span></td>
      </tr>
      <tr>
        <td id="L1028" class="blob-num js-line-number" data-line-number="1028"></td>
        <td id="LC1028" class="blob-code blob-code-inner js-file-line"><span class="pl-s">                    10 000 iterations usually converges</span></td>
      </tr>
      <tr>
        <td id="L1029" class="blob-num js-line-number" data-line-number="1029"></td>
        <td id="LC1029" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L1030" class="blob-num js-line-number" data-line-number="1030"></td>
        <td id="LC1030" class="blob-code blob-code-inner js-file-line"><span class="pl-s">===================================================================================</span></td>
      </tr>
      <tr>
        <td id="L1031" class="blob-num js-line-number" data-line-number="1031"></td>
        <td id="LC1031" class="blob-code blob-code-inner js-file-line"><span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1032" class="blob-num js-line-number" data-line-number="1032"></td>
        <td id="LC1032" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1033" class="blob-num js-line-number" data-line-number="1033"></td>
        <td id="LC1033" class="blob-code blob-code-inner js-file-line">    references <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Chen, Jinsong, Andreas Kemna, and Susan S. Hubbard. 2008. “A Comparison between</span></td>
      </tr>
      <tr>
        <td id="L1034" class="blob-num js-line-number" data-line-number="1034"></td>
        <td id="LC1034" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Gauss-Newton and Markov-Chain Monte Carlo–based Methods for Inverting</span></td>
      </tr>
      <tr>
        <td id="L1035" class="blob-num js-line-number" data-line-number="1035"></td>
        <td id="LC1035" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Spectral Induced-Polarization Data for Cole-Cole Parameters.” Geophysics</span></td>
      </tr>
      <tr>
        <td id="L1036" class="blob-num js-line-number" data-line-number="1036"></td>
        <td id="LC1036" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    73 (6): F247–59. doi:10.1190/1.2976115.</span></td>
      </tr>
      <tr>
        <td id="L1037" class="blob-num js-line-number" data-line-number="1037"></td>
        <td id="LC1037" class="blob-code blob-code-inner js-file-line"><span class="pl-s">Dias, Carlos A. 2000. “Developments in a Model to Describe Low-Frequency</span></td>
      </tr>
      <tr>
        <td id="L1038" class="blob-num js-line-number" data-line-number="1038"></td>
        <td id="LC1038" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Electrical Polarization of Rocks.” Geophysics 65 (2): 437–51.</span></td>
      </tr>
      <tr>
        <td id="L1039" class="blob-num js-line-number" data-line-number="1039"></td>
        <td id="LC1039" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    doi:10.1190/1.1444738.</span></td>
      </tr>
      <tr>
        <td id="L1040" class="blob-num js-line-number" data-line-number="1040"></td>
        <td id="LC1040" class="blob-code blob-code-inner js-file-line"><span class="pl-s">Gamerman, Dani, and Hedibert F. Lopes. 2006. Markov Chain Monte Carlo:</span></td>
      </tr>
      <tr>
        <td id="L1041" class="blob-num js-line-number" data-line-number="1041"></td>
        <td id="LC1041" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Stochastic Simulation for Bayesian Inference, Second Edition. CRC Press.</span></td>
      </tr>
      <tr>
        <td id="L1042" class="blob-num js-line-number" data-line-number="1042"></td>
        <td id="LC1042" class="blob-code blob-code-inner js-file-line"><span class="pl-s">Ghorbani, A., C. Camerlynck, N. Florsch, P. Cosenza, and A. Revil. 2007.</span></td>
      </tr>
      <tr>
        <td id="L1043" class="blob-num js-line-number" data-line-number="1043"></td>
        <td id="LC1043" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    “Bayesian Inference of the Cole–Cole Parameters from Time- and Frequency-</span></td>
      </tr>
      <tr>
        <td id="L1044" class="blob-num js-line-number" data-line-number="1044"></td>
        <td id="LC1044" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Domain Induced Polarization.” Geophysical Prospecting 55 (4): 589–605.</span></td>
      </tr>
      <tr>
        <td id="L1045" class="blob-num js-line-number" data-line-number="1045"></td>
        <td id="LC1045" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    doi:10.1111/j.1365-2478.2007.00627.x.</span></td>
      </tr>
      <tr>
        <td id="L1046" class="blob-num js-line-number" data-line-number="1046"></td>
        <td id="LC1046" class="blob-code blob-code-inner js-file-line"><span class="pl-s">Hoff, Peter D. 2009. A First Course in Bayesian Statistical Methods. Springer</span></td>
      </tr>
      <tr>
        <td id="L1047" class="blob-num js-line-number" data-line-number="1047"></td>
        <td id="LC1047" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Science &amp; Business Media.</span></td>
      </tr>
      <tr>
        <td id="L1048" class="blob-num js-line-number" data-line-number="1048"></td>
        <td id="LC1048" class="blob-code blob-code-inner js-file-line"><span class="pl-s">Keery, John, Andrew Binley, Ahmed Elshenawy, and Jeremy Clifford. 2012.</span></td>
      </tr>
      <tr>
        <td id="L1049" class="blob-num js-line-number" data-line-number="1049"></td>
        <td id="LC1049" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    “Markov-Chain Monte Carlo Estimation of Distributed Debye Relaxations in</span></td>
      </tr>
      <tr>
        <td id="L1050" class="blob-num js-line-number" data-line-number="1050"></td>
        <td id="LC1050" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Spectral Induced Polarization.” Geophysics 77 (2): E159–70.</span></td>
      </tr>
      <tr>
        <td id="L1051" class="blob-num js-line-number" data-line-number="1051"></td>
        <td id="LC1051" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    doi:10.1190/geo2011-0244.1.</span></td>
      </tr>
      <tr>
        <td id="L1052" class="blob-num js-line-number" data-line-number="1052"></td>
        <td id="LC1052" class="blob-code blob-code-inner js-file-line"><span class="pl-s">Nordsiek, Sven, and Andreas Weller. 2008. “A New Approach to Fitting Induced-</span></td>
      </tr>
      <tr>
        <td id="L1053" class="blob-num js-line-number" data-line-number="1053"></td>
        <td id="LC1053" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Polarization Spectra.” Geophysics 73 (6): F235–45. doi:10.1190/1.2987412.</span></td>
      </tr>
      <tr>
        <td id="L1054" class="blob-num js-line-number" data-line-number="1054"></td>
        <td id="LC1054" class="blob-code blob-code-inner js-file-line"><span class="pl-s">Patil, A., D. Huard and C.J. Fonnesbeck. 2010. PyMC: Bayesian Stochastic</span></td>
      </tr>
      <tr>
        <td id="L1055" class="blob-num js-line-number" data-line-number="1055"></td>
        <td id="LC1055" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Modelling in Python. Journal of Statistical Software, 35(4), pp. 1-81</span></td>
      </tr>
      <tr>
        <td id="L1056" class="blob-num js-line-number" data-line-number="1056"></td>
        <td id="LC1056" class="blob-code blob-code-inner js-file-line"><span class="pl-s">Pelton, W. H., W. R. Sill, and B. D. Smith. 1983. Interpretation of Complex</span></td>
      </tr>
      <tr>
        <td id="L1057" class="blob-num js-line-number" data-line-number="1057"></td>
        <td id="LC1057" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Resistivity and Dielectric Data — Part 1. Vol 29. Geophysical Transactions.</span></td>
      </tr>
      <tr>
        <td id="L1058" class="blob-num js-line-number" data-line-number="1058"></td>
        <td id="LC1058" class="blob-code blob-code-inner js-file-line"><span class="pl-s">Pelton, W. H., S. H. Ward, P. G. Hallof, W. R. Sill, and P. H. Nelson. 1978.</span></td>
      </tr>
      <tr>
        <td id="L1059" class="blob-num js-line-number" data-line-number="1059"></td>
        <td id="LC1059" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    “Mineral Discrimination and Removal of Inductive Coupling with</span></td>
      </tr>
      <tr>
        <td id="L1060" class="blob-num js-line-number" data-line-number="1060"></td>
        <td id="LC1060" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Multifrequency IP.” Geophysics 43 (3): 588–609. doi:10.1190/1.1440839.<span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1061" class="blob-num js-line-number" data-line-number="1061"></td>
        <td id="LC1061" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1062" class="blob-num js-line-number" data-line-number="1062"></td>
        <td id="LC1062" class="blob-code blob-code-inner js-file-line">    license_info <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>The MIT License (MIT)</span></td>
      </tr>
      <tr>
        <td id="L1063" class="blob-num js-line-number" data-line-number="1063"></td>
        <td id="LC1063" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L1064" class="blob-num js-line-number" data-line-number="1064"></td>
        <td id="LC1064" class="blob-code blob-code-inner js-file-line"><span class="pl-s">Copyright (c) 2016 Charles L. Bérubé</span></td>
      </tr>
      <tr>
        <td id="L1065" class="blob-num js-line-number" data-line-number="1065"></td>
        <td id="LC1065" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L1066" class="blob-num js-line-number" data-line-number="1066"></td>
        <td id="LC1066" class="blob-code blob-code-inner js-file-line"><span class="pl-s">Permission is hereby granted, free of charge, to any person obtaining a copy</span></td>
      </tr>
      <tr>
        <td id="L1067" class="blob-num js-line-number" data-line-number="1067"></td>
        <td id="LC1067" class="blob-code blob-code-inner js-file-line"><span class="pl-s">of this software and associated documentation files (the &quot;Software&quot;), to deal</span></td>
      </tr>
      <tr>
        <td id="L1068" class="blob-num js-line-number" data-line-number="1068"></td>
        <td id="LC1068" class="blob-code blob-code-inner js-file-line"><span class="pl-s">in the Software without restriction, including without limitation the rights</span></td>
      </tr>
      <tr>
        <td id="L1069" class="blob-num js-line-number" data-line-number="1069"></td>
        <td id="LC1069" class="blob-code blob-code-inner js-file-line"><span class="pl-s">to use, copy, modify, merge, publish, distribute, sublicense, and/or sell</span></td>
      </tr>
      <tr>
        <td id="L1070" class="blob-num js-line-number" data-line-number="1070"></td>
        <td id="LC1070" class="blob-code blob-code-inner js-file-line"><span class="pl-s">copies of the Software, and to permit persons to whom the Software is</span></td>
      </tr>
      <tr>
        <td id="L1071" class="blob-num js-line-number" data-line-number="1071"></td>
        <td id="LC1071" class="blob-code blob-code-inner js-file-line"><span class="pl-s">furnished to do so, subject to the following conditions:</span></td>
      </tr>
      <tr>
        <td id="L1072" class="blob-num js-line-number" data-line-number="1072"></td>
        <td id="LC1072" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L1073" class="blob-num js-line-number" data-line-number="1073"></td>
        <td id="LC1073" class="blob-code blob-code-inner js-file-line"><span class="pl-s">The above copyright notice and this permission notice shall be included in all</span></td>
      </tr>
      <tr>
        <td id="L1074" class="blob-num js-line-number" data-line-number="1074"></td>
        <td id="LC1074" class="blob-code blob-code-inner js-file-line"><span class="pl-s">copies or substantial portions of the Software.</span></td>
      </tr>
      <tr>
        <td id="L1075" class="blob-num js-line-number" data-line-number="1075"></td>
        <td id="LC1075" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L1076" class="blob-num js-line-number" data-line-number="1076"></td>
        <td id="LC1076" class="blob-code blob-code-inner js-file-line"><span class="pl-s">THE SOFTWARE IS PROVIDED &quot;AS IS&quot;, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR</span></td>
      </tr>
      <tr>
        <td id="L1077" class="blob-num js-line-number" data-line-number="1077"></td>
        <td id="LC1077" class="blob-code blob-code-inner js-file-line"><span class="pl-s">IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,</span></td>
      </tr>
      <tr>
        <td id="L1078" class="blob-num js-line-number" data-line-number="1078"></td>
        <td id="LC1078" class="blob-code blob-code-inner js-file-line"><span class="pl-s">FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE</span></td>
      </tr>
      <tr>
        <td id="L1079" class="blob-num js-line-number" data-line-number="1079"></td>
        <td id="LC1079" class="blob-code blob-code-inner js-file-line"><span class="pl-s">AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER</span></td>
      </tr>
      <tr>
        <td id="L1080" class="blob-num js-line-number" data-line-number="1080"></td>
        <td id="LC1080" class="blob-code blob-code-inner js-file-line"><span class="pl-s">LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,</span></td>
      </tr>
      <tr>
        <td id="L1081" class="blob-num js-line-number" data-line-number="1081"></td>
        <td id="LC1081" class="blob-code blob-code-inner js-file-line"><span class="pl-s">OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE</span></td>
      </tr>
      <tr>
        <td id="L1082" class="blob-num js-line-number" data-line-number="1082"></td>
        <td id="LC1082" class="blob-code blob-code-inner js-file-line"><span class="pl-s">SOFTWARE.</span></td>
      </tr>
      <tr>
        <td id="L1083" class="blob-num js-line-number" data-line-number="1083"></td>
        <td id="LC1083" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L1084" class="blob-num js-line-number" data-line-number="1084"></td>
        <td id="LC1084" class="blob-code blob-code-inner js-file-line"><span class="pl-s">https://opensource.org/licenses/MIT</span></td>
      </tr>
      <tr>
        <td id="L1085" class="blob-num js-line-number" data-line-number="1085"></td>
        <td id="LC1085" class="blob-code blob-code-inner js-file-line"><span class="pl-s">https://github.com/clberube/bisip</span></td>
      </tr>
      <tr>
        <td id="L1086" class="blob-num js-line-number" data-line-number="1086"></td>
        <td id="LC1086" class="blob-code blob-code-inner js-file-line"><span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1087" class="blob-num js-line-number" data-line-number="1087"></td>
        <td id="LC1087" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1088" class="blob-num js-line-number" data-line-number="1088"></td>
        <td id="LC1088" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">popup</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">title</span>, <span class="pl-smi">message</span>, <span class="pl-smi">size</span><span class="pl-k">=</span><span class="pl-c1">10</span>):</td>
      </tr>
      <tr>
        <td id="L1089" class="blob-num js-line-number" data-line-number="1089"></td>
        <td id="LC1089" class="blob-code blob-code-inner js-file-line">        top <span class="pl-k">=</span> tk.Toplevel()</td>
      </tr>
      <tr>
        <td id="L1090" class="blob-num js-line-number" data-line-number="1090"></td>
        <td id="LC1090" class="blob-code blob-code-inner js-file-line">        top.title(title)</td>
      </tr>
      <tr>
        <td id="L1091" class="blob-num js-line-number" data-line-number="1091"></td>
        <td id="LC1091" class="blob-code blob-code-inner js-file-line">        about_message <span class="pl-k">=</span> (message)</td>
      </tr>
      <tr>
        <td id="L1092" class="blob-num js-line-number" data-line-number="1092"></td>
        <td id="LC1092" class="blob-code blob-code-inner js-file-line">        top.lift()</td>
      </tr>
      <tr>
        <td id="L1093" class="blob-num js-line-number" data-line-number="1093"></td>
        <td id="LC1093" class="blob-code blob-code-inner js-file-line">        msg <span class="pl-k">=</span> tk.Text(top, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">90</span>, <span class="pl-v">font</span><span class="pl-k">=</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>courier<span class="pl-pds">&#39;</span></span>, size, <span class="pl-s"><span class="pl-pds">&#39;</span>normal<span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="L1094" class="blob-num js-line-number" data-line-number="1094"></td>
        <td id="LC1094" class="blob-code blob-code-inner js-file-line">        msg.grid(<span class="pl-v">stick</span><span class="pl-k">=</span>tk.N, <span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">10</span>,<span class="pl-c1">10</span>), <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">10</span>,<span class="pl-c1">10</span>))</td>
      </tr>
      <tr>
        <td id="L1095" class="blob-num js-line-number" data-line-number="1095"></td>
        <td id="LC1095" class="blob-code blob-code-inner js-file-line">        msg.insert(<span class="pl-s"><span class="pl-pds">&quot;</span>1.0<span class="pl-pds">&quot;</span></span>, about_message)</td>
      </tr>
      <tr>
        <td id="L1096" class="blob-num js-line-number" data-line-number="1096"></td>
        <td id="LC1096" class="blob-code blob-code-inner js-file-line">        button <span class="pl-k">=</span> tk.Button(top, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">20</span>, <span class="pl-v">text</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Dismiss<span class="pl-pds">&quot;</span></span>, <span class="pl-v">command</span><span class="pl-k">=</span>top.destroy, <span class="pl-v">bg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>gray97<span class="pl-pds">&#39;</span></span>, <span class="pl-v">relief</span><span class="pl-k">=</span>tk.<span class="pl-c1">GROOVE</span>)</td>
      </tr>
      <tr>
        <td id="L1097" class="blob-num js-line-number" data-line-number="1097"></td>
        <td id="LC1097" class="blob-code blob-code-inner js-file-line">        button.grid(<span class="pl-v">sticky</span><span class="pl-k">=</span>tk.S, <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">0</span>,<span class="pl-c1">10</span>))</td>
      </tr>
      <tr>
        <td id="L1098" class="blob-num js-line-number" data-line-number="1098"></td>
        <td id="LC1098" class="blob-code blob-code-inner js-file-line">        s <span class="pl-k">=</span> tk.Scrollbar(top, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">20</span>)</td>
      </tr>
      <tr>
        <td id="L1099" class="blob-num js-line-number" data-line-number="1099"></td>
        <td id="LC1099" class="blob-code blob-code-inner js-file-line">        s.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">sticky</span><span class="pl-k">=</span>tk.E<span class="pl-k">+</span>tk.N<span class="pl-k">+</span>tk.S, <span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">0</span>,<span class="pl-c1">10</span>),<span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">10</span>,<span class="pl-c1">10</span>))</td>
      </tr>
      <tr>
        <td id="L1100" class="blob-num js-line-number" data-line-number="1100"></td>
        <td id="LC1100" class="blob-code blob-code-inner js-file-line">        s[<span class="pl-s"><span class="pl-pds">&#39;</span>command<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> msg.yview</td>
      </tr>
      <tr>
        <td id="L1101" class="blob-num js-line-number" data-line-number="1101"></td>
        <td id="LC1101" class="blob-code blob-code-inner js-file-line">        msg[<span class="pl-s"><span class="pl-pds">&#39;</span>yscrollcommand<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> s.set</td>
      </tr>
      <tr>
        <td id="L1102" class="blob-num js-line-number" data-line-number="1102"></td>
        <td id="LC1102" class="blob-code blob-code-inner js-file-line">        top.resizable(<span class="pl-v">width</span><span class="pl-k">=</span>tk.<span class="pl-c1">FALSE</span>, <span class="pl-v">height</span><span class="pl-k">=</span>tk.<span class="pl-c1">FALSE</span>)</td>
      </tr>
      <tr>
        <td id="L1103" class="blob-num js-line-number" data-line-number="1103"></td>
        <td id="LC1103" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1104" class="blob-num js-line-number" data-line-number="1104"></td>
        <td id="LC1104" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">about</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">fontz</span>):</td>
      </tr>
      <tr>
        <td id="L1105" class="blob-num js-line-number" data-line-number="1105"></td>
        <td id="LC1105" class="blob-code blob-code-inner js-file-line">        top <span class="pl-k">=</span> tk.Toplevel()</td>
      </tr>
      <tr>
        <td id="L1106" class="blob-num js-line-number" data-line-number="1106"></td>
        <td id="LC1106" class="blob-code blob-code-inner js-file-line">        top.title(<span class="pl-s"><span class="pl-pds">&quot;</span>About<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1107" class="blob-num js-line-number" data-line-number="1107"></td>
        <td id="LC1107" class="blob-code blob-code-inner js-file-line">        top.lift()</td>
      </tr>
      <tr>
        <td id="L1108" class="blob-num js-line-number" data-line-number="1108"></td>
        <td id="LC1108" class="blob-code blob-code-inner js-file-line">        tk.Label(top,</td>
      </tr>
      <tr>
        <td id="L1109" class="blob-num js-line-number" data-line-number="1109"></td>
        <td id="LC1109" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">text</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Bayesian inversion of spectral induced polarization data<span class="pl-pds">&quot;&quot;&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L1110" class="blob-num js-line-number" data-line-number="1110"></td>
        <td id="LC1110" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">justify</span> <span class="pl-k">=</span> tk.<span class="pl-c1">CENTER</span>, <span class="pl-v">font</span><span class="pl-k">=</span>fontz[<span class="pl-s"><span class="pl-pds">&quot;</span>bold<span class="pl-pds">&quot;</span></span>]).grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>,<span class="pl-v">columnspan</span><span class="pl-k">=</span><span class="pl-c1">2</span>,<span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">10</span>,<span class="pl-c1">10</span>), <span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">10</span>,<span class="pl-c1">10</span>))</td>
      </tr>
      <tr>
        <td id="L1111" class="blob-num js-line-number" data-line-number="1111"></td>
        <td id="LC1111" class="blob-code blob-code-inner js-file-line">        tk.Label(top,</td>
      </tr>
      <tr>
        <td id="L1112" class="blob-num js-line-number" data-line-number="1112"></td>
        <td id="LC1112" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">text</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>2015-2016</span></td>
      </tr>
      <tr>
        <td id="L1113" class="blob-num js-line-number" data-line-number="1113"></td>
        <td id="LC1113" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    École Polytechnique de Montréal</span></td>
      </tr>
      <tr>
        <td id="L1114" class="blob-num js-line-number" data-line-number="1114"></td>
        <td id="LC1114" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Groupe de recherche en géophysique appliquée</span></td>
      </tr>
      <tr>
        <td id="L1115" class="blob-num js-line-number" data-line-number="1115"></td>
        <td id="LC1115" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L1116" class="blob-num js-line-number" data-line-number="1116"></td>
        <td id="LC1116" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">justify</span> <span class="pl-k">=</span> tk.<span class="pl-c1">CENTER</span>).grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>,<span class="pl-v">columnspan</span><span class="pl-k">=</span><span class="pl-c1">2</span>, <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">10</span>,<span class="pl-c1">10</span>), <span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">10</span>,<span class="pl-c1">10</span>))</td>
      </tr>
      <tr>
        <td id="L1117" class="blob-num js-line-number" data-line-number="1117"></td>
        <td id="LC1117" class="blob-code blob-code-inner js-file-line">        tk.Label(top,</td>
      </tr>
      <tr>
        <td id="L1118" class="blob-num js-line-number" data-line-number="1118"></td>
        <td id="LC1118" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">text</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Contact:<span class="pl-pds">&quot;&quot;&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L1119" class="blob-num js-line-number" data-line-number="1119"></td>
        <td id="LC1119" class="blob-code blob-code-inner js-file-line">                  <span class="pl-v">justify</span> <span class="pl-k">=</span> tk.<span class="pl-c1">CENTER</span>).grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">2</span>, <span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>,<span class="pl-v">columnspan</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">10</span>,<span class="pl-c1">10</span>), <span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">10</span>,<span class="pl-c1">10</span>))</td>
      </tr>
      <tr>
        <td id="L1120" class="blob-num js-line-number" data-line-number="1120"></td>
        <td id="LC1120" class="blob-code blob-code-inner js-file-line">        about_message <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>cberube@ageophysics.com<span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1121" class="blob-num js-line-number" data-line-number="1121"></td>
        <td id="LC1121" class="blob-code blob-code-inner js-file-line">        msg <span class="pl-k">=</span> tk.Text(top, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">27</span>)</td>
      </tr>
      <tr>
        <td id="L1122" class="blob-num js-line-number" data-line-number="1122"></td>
        <td id="LC1122" class="blob-code blob-code-inner js-file-line">        msg.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">2</span>,<span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">1</span>,<span class="pl-v">padx</span><span class="pl-k">=</span>(<span class="pl-c1">10</span>,<span class="pl-c1">10</span>), <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">10</span>,<span class="pl-c1">10</span>))</td>
      </tr>
      <tr>
        <td id="L1123" class="blob-num js-line-number" data-line-number="1123"></td>
        <td id="LC1123" class="blob-code blob-code-inner js-file-line">        msg.insert(<span class="pl-s"><span class="pl-pds">&quot;</span>1.0<span class="pl-pds">&quot;</span></span>, about_message)</td>
      </tr>
      <tr>
        <td id="L1124" class="blob-num js-line-number" data-line-number="1124"></td>
        <td id="LC1124" class="blob-code blob-code-inner js-file-line">        button <span class="pl-k">=</span> tk.Button(top, <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">20</span>, <span class="pl-v">text</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Dismiss<span class="pl-pds">&quot;</span></span>, <span class="pl-v">command</span><span class="pl-k">=</span>top.destroy, <span class="pl-v">bg</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>gray97<span class="pl-pds">&#39;</span></span>, <span class="pl-v">relief</span><span class="pl-k">=</span>tk.<span class="pl-c1">GROOVE</span>)</td>
      </tr>
      <tr>
        <td id="L1125" class="blob-num js-line-number" data-line-number="1125"></td>
        <td id="LC1125" class="blob-code blob-code-inner js-file-line">        button.grid(<span class="pl-v">row</span><span class="pl-k">=</span><span class="pl-c1">3</span>,<span class="pl-v">column</span><span class="pl-k">=</span><span class="pl-c1">0</span>,<span class="pl-v">columnspan</span><span class="pl-k">=</span><span class="pl-c1">2</span>,<span class="pl-v">sticky</span><span class="pl-k">=</span>tk.S, <span class="pl-v">pady</span><span class="pl-k">=</span>(<span class="pl-c1">0</span>,<span class="pl-c1">10</span>))</td>
      </tr>
      <tr>
        <td id="L1126" class="blob-num js-line-number" data-line-number="1126"></td>
        <td id="LC1126" class="blob-code blob-code-inner js-file-line">        top.resizable(<span class="pl-v">width</span><span class="pl-k">=</span>tk.<span class="pl-c1">FALSE</span>, <span class="pl-v">height</span><span class="pl-k">=</span>tk.<span class="pl-c1">FALSE</span>)</td>
      </tr>
      <tr>
        <td id="L1127" class="blob-num js-line-number" data-line-number="1127"></td>
        <td id="LC1127" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1128" class="blob-num js-line-number" data-line-number="1128"></td>
        <td id="LC1128" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>==============================================================================</span></td>
      </tr>
      <tr>
        <td id="L1129" class="blob-num js-line-number" data-line-number="1129"></td>
        <td id="LC1129" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Main function</span></td>
      </tr>
      <tr>
        <td id="L1130" class="blob-num js-line-number" data-line-number="1130"></td>
        <td id="LC1130" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>==============================================================================</span></td>
      </tr>
      <tr>
        <td id="L1131" class="blob-num js-line-number" data-line-number="1131"></td>
        <td id="LC1131" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">launch</span>():</td>
      </tr>
      <tr>
        <td id="L1132" class="blob-num js-line-number" data-line-number="1132"></td>
        <td id="LC1132" class="blob-code blob-code-inner js-file-line">    root <span class="pl-k">=</span> tk.Tk()</td>
      </tr>
      <tr>
        <td id="L1133" class="blob-num js-line-number" data-line-number="1133"></td>
        <td id="LC1133" class="blob-code blob-code-inner js-file-line">    root.wm_title(<span class="pl-s"><span class="pl-pds">&quot;</span>Bayesian inversion of SIP data<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1134" class="blob-num js-line-number" data-line-number="1134"></td>
        <td id="LC1134" class="blob-code blob-code-inner js-file-line">    root.option_add(<span class="pl-s"><span class="pl-pds">&quot;</span>*Font<span class="pl-pds">&quot;</span></span>, window_font)</td>
      </tr>
      <tr>
        <td id="L1135" class="blob-num js-line-number" data-line-number="1135"></td>
        <td id="LC1135" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span>==============================================================================</span></td>
      </tr>
      <tr>
        <td id="L1136" class="blob-num js-line-number" data-line-number="1136"></td>
        <td id="LC1136" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> For MacOS, bring the window to front</span></td>
      </tr>
      <tr>
        <td id="L1137" class="blob-num js-line-number" data-line-number="1137"></td>
        <td id="LC1137" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Without these lines the application will start in background</span></td>
      </tr>
      <tr>
        <td id="L1138" class="blob-num js-line-number" data-line-number="1138"></td>
        <td id="LC1138" class="blob-code blob-code-inner js-file-line">    root.lift()</td>
      </tr>
      <tr>
        <td id="L1139" class="blob-num js-line-number" data-line-number="1139"></td>
        <td id="LC1139" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Darwin<span class="pl-pds">&quot;</span></span> <span class="pl-k">in</span> system():</td>
      </tr>
      <tr>
        <td id="L1140" class="blob-num js-line-number" data-line-number="1140"></td>
        <td id="LC1140" class="blob-code blob-code-inner js-file-line">        root.call(<span class="pl-s"><span class="pl-pds">&#39;</span>wm<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>attributes<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>-topmost<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L1141" class="blob-num js-line-number" data-line-number="1141"></td>
        <td id="LC1141" class="blob-code blob-code-inner js-file-line">        root.after_idle(root.call, <span class="pl-s"><span class="pl-pds">&#39;</span>wm<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>attributes<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>-topmost<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L1142" class="blob-num js-line-number" data-line-number="1142"></td>
        <td id="LC1142" class="blob-code blob-code-inner js-file-line">    app <span class="pl-k">=</span> MainApplication(root, fontz)</td>
      </tr>
      <tr>
        <td id="L1143" class="blob-num js-line-number" data-line-number="1143"></td>
        <td id="LC1143" class="blob-code blob-code-inner js-file-line">    root.mainloop()</td>
      </tr>
      <tr>
        <td id="L1144" class="blob-num js-line-number" data-line-number="1144"></td>
        <td id="LC1144" class="blob-code blob-code-inner js-file-line">    app.save()</td>
      </tr>
      <tr>
        <td id="L1145" class="blob-num js-line-number" data-line-number="1145"></td>
        <td id="LC1145" class="blob-code blob-code-inner js-file-line"><span class="pl-k">if</span> <span class="pl-c1">__name__</span> <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>__launch__<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L1146" class="blob-num js-line-number" data-line-number="1146"></td>
        <td id="LC1146" class="blob-code blob-code-inner js-file-line">    launch()</td>
      </tr>
</table>

  <details class="details-reset details-overlay BlobToolbar position-absolute js-file-line-actions dropdown d-none" aria-hidden="true">
    <summary class="btn-octicon ml-0 px-2 p-0 bg-white border border-gray-dark rounded-1" aria-label="Inline file action toolbar">
      <svg class="octicon octicon-kebab-horizontal" viewBox="0 0 13 16" version="1.1" width="13" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3zm5 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3zM13 7.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0z"/></svg>
    </summary>
    <details-menu>
      <ul class="BlobToolbar-dropdown dropdown-menu dropdown-menu-se mt-2" style="width:185px">
        <li><clipboard-copy role="menuitem" class="dropdown-item" id="js-copy-lines" style="cursor:pointer;" data-original-text="Copy lines">Copy lines</clipboard-copy></li>
        <li><clipboard-copy role="menuitem" class="dropdown-item" id="js-copy-permalink" style="cursor:pointer;" data-original-text="Copy permalink">Copy permalink</clipboard-copy></li>
        <li><a class="dropdown-item js-update-url-with-hash" id="js-view-git-blame" role="menuitem" href="/clberube/BISIP/blame/5b08fc447e6ac66fc9a50c441b9cc2155725d018/bisip/GUI.py">View git blame</a></li>
          <li><a class="dropdown-item" id="js-new-issue" role="menuitem" href="/clberube/BISIP/issues/new">Reference in new issue</a></li>
      </ul>
    </details-menu>
  </details>

  </div>

    </div>

  

  <details class="details-reset details-overlay details-overlay-dark">
    <summary data-hotkey="l" aria-label="Jump to line"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast linejump" aria-label="Jump to line">
      <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-jump-to-line-form Box-body d-flex" action="" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
        <input class="form-control flex-auto mr-3 linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
        <button type="submit" class="btn" data-close-dialog>Go</button>
</form>    </details-dialog>
  </details>



  </div>
  <div class="modal-backdrop js-touch-events"></div>
</div>

    </main>
  </div>
  

  </div>

        
<div class="footer container-lg width-full p-responsive" role="contentinfo">
  <div class="position-relative d-flex flex-row-reverse flex-lg-row flex-wrap flex-lg-nowrap flex-justify-center flex-lg-justify-between pt-6 pb-2 mt-6 f6 text-gray border-top border-gray-light ">
    <ul class="list-style-none d-flex flex-wrap col-12 col-lg-5 flex-justify-center flex-lg-justify-between mb-2 mb-lg-0">
      <li class="mr-3 mr-lg-0">&copy; 2019 <span title="0.20393s from unicorn-64c76b4b8f-vvzr6">GitHub</span>, Inc.</li>
        <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to terms, text:terms" href="https://github.com/site/terms">Terms</a></li>
        <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to privacy, text:privacy" href="https://github.com/site/privacy">Privacy</a></li>
        <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to security, text:security" href="https://github.com/security">Security</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://githubstatus.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a data-ga-click="Footer, go to help, text:help" href="https://help.github.com">Help</a></li>
    </ul>

    <a aria-label="Homepage" title="GitHub" class="footer-octicon d-none d-lg-block mx-lg-4" href="https://github.com">
      <svg height="24" class="octicon octicon-mark-github" viewBox="0 0 16 16" version="1.1" width="24" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>
   <ul class="list-style-none d-flex flex-wrap col-12 col-lg-5 flex-justify-center flex-lg-justify-between mb-2 mb-lg-0">
        <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to contact, text:contact" href="https://github.com/contact">Contact GitHub</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://github.com/pricing" data-ga-click="Footer, go to Pricing, text:Pricing">Pricing</a></li>
      <li class="mr-3 mr-lg-0"><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li class="mr-3 mr-lg-0"><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://github.blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a data-ga-click="Footer, go to about, text:about" href="https://github.com/about">About</a></li>

    </ul>
  </div>
  <div class="d-flex flex-justify-center pb-6">
    <span class="f6 text-gray-light"></span>
  </div>
</div>



  <div id="ajax-error-message" class="ajax-error-message flash flash-error">
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 0 0 0 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 0 0 .01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z"/></svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
    </button>
    You can’t perform that action at this time.
  </div>


    
    <script crossorigin="anonymous" integrity="sha512-g8y61ukpuxDEU1w0B8AaXzCoZO9ZV7aUNRgrgUpMNaHulIZN5RB/pxmSXMScAroJfjz4IQFOfAZXod3O+htchg==" type="application/javascript" src="https://github.githubassets.com/assets/frameworks-341d995f.js"></script>
    
    <script crossorigin="anonymous" async="async" integrity="sha512-nWnoUeKrGoM2pM/rLqZn/tolJjPX4nYPzlgNe2vR8Qfy0VS4LlzTwf6oiN7zmQqjswJ8/0c5LRLbd9ZQ7+NUtQ==" type="application/javascript" src="https://github.githubassets.com/assets/github-bootstrap-6b12f7d4.js"></script>
    
    
    
  <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner" hidden
    >
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 0 0 0 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 0 0 .01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z"/></svg>
    <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
  </div>
  <template id="site-details-dialog">
  <details class="details-reset details-overlay details-overlay-dark lh-default text-gray-dark hx_rsm" open>
    <summary role="button" aria-label="Close dialog"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast hx_rsm-dialog hx_rsm-modal">
      <button class="Box-btn-octicon m-0 btn-octicon position-absolute right-0 top-0" type="button" aria-label="Close dialog" data-close-dialog>
        <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
      </button>
      <div class="octocat-spinner my-6 js-details-dialog-spinner"></div>
    </details-dialog>
  </details>
</template>

  <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box box-shadow-large" style="width:360px;">
  </div>
</div>

  <div aria-live="polite" class="js-global-screen-reader-notice sr-only"></div>

  </body>
</html>

