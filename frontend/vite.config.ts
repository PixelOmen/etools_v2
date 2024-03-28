import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [svelte()],
  build: {
    outDir: '../src/svelteflask/static',
  },
  server: {
    proxy: {
      '/api': 'http://localhost:4090/'
    }
  }
})
