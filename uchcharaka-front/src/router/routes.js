
export default [
  {
    path: '/',
    redirect: '/transcriber'
  },

  {
    path: '/web-api',
    component: () => import('layouts/default'),
    children: [
      { path: '', component: () => import('pages/web-api') }
    ]
  },

  {
    path: '/python',
    component: () => import('layouts/default'),
    children: [
      { path: '', component: () => import('pages/python') }
    ]
  },

  {
    path: '/notes',
    component: () => import('layouts/default'),
    children: [
      { path: '', component: () => import('pages/notes') }
    ]
  },

  {
    path: '/pronunciation',
    component: () => import('layouts/default'),
    children: [
      { path: '', component: () => import('pages/pronunciation') }
    ]
  },

  {
    path: '/documentation',
    component: () => import('layouts/default'),
    children: [
      { path: '', component: () => import('pages/documentation') }
    ]
  },

  {
    path: '/help',
    component: () => import('layouts/default'),
    children: [
      { path: '', component: () => import('pages/help') }
    ]
  },

  {
    path: '/texts/:text',
    component: () => import('layouts/default'),
    children: [
      { path: '', component: () => import('pages/texts') }
    ]
  },

  {
    path: '/about',
    component: () => import('layouts/default'),
    children: [
      { path: '', component: () => import('pages/about') }
    ]
  },

  {
    path: '/transcriber',
    component: () => import('layouts/default'),
    children: [
      { path: '', component: () => import('pages/index') }
    ]
  },

  { // Always leave this as last one
    path: '*',
    redirect: '/transcriber'
  }
]
