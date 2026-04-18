import { resolve } from 'path'
import { defineConfig } from 'vite'

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        home: resolve(__dirname, 'home/index.html'),
        who_we_are: resolve(__dirname, 'who_we_are/index.html'),
        gallery: resolve(__dirname, 'gallery/index.html'),
        contact_us: resolve(__dirname, 'contact_us/index.html'),
      },
    },
  },
})
