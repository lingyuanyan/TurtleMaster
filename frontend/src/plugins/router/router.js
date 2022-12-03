import { createRouter, createWebHistory } from 'vue-router';
import { userRoleEnum } from "../../types/index"

import TopBanner from "../../components/banner.vue";
import FrontDoor from "../../pages/FrontDoor";
import FooterBar from "../../components/footer.vue";

const router = createRouter({
    history: createWebHistory(),
    routes: [
        // guest
        {
            name: 'front-door',
            path: '/',
            meta: {
                title: 'TurtleMaster Club\'s CovidHub',
                requiredRoles: [userRoleEnum.NONE],
                metaTags: [
                    {
                        name: 'description',
                        content: 'The home page of TurtleMaster Club\'s CovidHub.'
                    },
                    {
                        property: 'og:description',
                        content: 'The home page of TurtleMaster Club\'s CovidHub.'
                    }
                ],
            },
            components: { default: FrontDoor, footer: FooterBar, header: TopBanner },
            /*children: [
              {
                name: 'team-members',
                path: ':teamId',
                component: TeamMembers,
                props: true
              } // /teams/t1
            ]*/
        },
    ],

    linkActiveClass: 'active',
    /*    scrollBehavior(_, _2, savedPosition) {
          if (savedPosition) {
            return savedPosition;
          }
          return { left: 0, top: 0 };
        }
    */
});


router.beforeEach(function (to, from, next) {
    to;
    from;
    // This goes through the matched routes from last to first, finding the closest route with a title.
    // e.g., if we have `/some/deep/nested/route` and `/some`, `/deep`, and `/nested` have titles,
    // `/nested`'s will be chosen.
    const nearestWithTitle = to.matched.slice().reverse().find(r => r.meta && r.meta.title);

    // Find the nearest route element with meta tags.
    const nearestWithMeta = to.matched.slice().reverse().find(r => r.meta && r.meta.metaTags);

    const previousNearestWithMeta = from.matched.slice().reverse().find(r => r.meta && r.meta.metaTags);

    // If a route with a title was found, set the document (page) title to that value.
    if (nearestWithTitle) {
        document.title = nearestWithTitle.meta.title;
    } else if (previousNearestWithMeta) {
        document.title = previousNearestWithMeta.meta.title;
    }

    // Remove any stale meta tags from the document using the key attribute we set below.
    Array.from(document.querySelectorAll('[data-vue-router-controlled]')).map(el => el.parentNode.removeChild(el));

    // Skip rendering meta tags if there are none.
    if (!nearestWithMeta) return next();

    // Turn the meta tag definitions into actual elements in the head.
    nearestWithMeta.meta.metaTags.map(tagDef => {
        const tag = document.createElement('meta');

        Object.keys(tagDef).forEach(key => {
            tag.setAttribute(key, tagDef[key]);
        });

        // We use this to track which meta tags we create so we don't interfere with other ones.
        tag.setAttribute('data-vue-router-controlled', '');

        return tag;
    })
        // Add the meta tags to the document head.
        .forEach(tag => document.head.appendChild(tag));

    next();
});


router.afterEach(function (to, from) {
    to;
    from;
});


export { router };