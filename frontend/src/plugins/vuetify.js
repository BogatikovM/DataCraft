// src/plugins/vuetify.js
import 'vuetify/styles'  // Импорт базовых стилей Vuetify
import { createVuetify } from 'vuetify'

// Импорт иконок напрямую из vuetify/iconsets
import { mdi } from 'vuetify/lib/iconsets/mdi'  
import { aliases as faAliases, fa } from 'vuetify/lib/iconsets/fa'  

// Настройка иконок и тем на ваш выбор
export default createVuetify({
  theme: {
    defaultTheme: 'light',
  },
  icons: {
    defaultSet: 'mdi', // Если вы хотите использовать mdi по умолчанию
    aliases: faAliases,
    sets: {
      mdi,
      fa,
    },
  },
})
