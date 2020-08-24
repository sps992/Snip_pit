import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
    routes:[
        {
            path: '/',
            redirect: '/index'
        },
        {
            path: '/create',
            name: 'create',
            component: () => import('./components/Create.vue')
        },
        {
            path: '/edit/:id',
            name: 'edit',
            component: () => import('./components/Index.vue')
        },
    ]
})