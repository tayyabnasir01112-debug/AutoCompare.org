// @ts-check

import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
        site: 'https://autocompare.org',
        integrations: [mdx(), sitemap()],
        server: {
                host: '0.0.0.0',
                port: 5000
        },
        vite: {
                server: {
                        watch: {
                                usePolling: true
                        }
                }
        }
});
