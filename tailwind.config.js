/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./**/*.html'],
  darkMode: 'class',
  theme: {
    extend: {
      backgroundImage: {
        'header_img': "url('/public/img/common/bg-top-23_2.jpg')",
        'bg_nav': "url('/public/img/common/bg_nav.jpg')",
        'footer_img': "url('/public/img/common/bg-footer.jpg')",
        'bg_card': "url('/public/img/common/bg_card.png')"
      }
    },
    screens: {
      lg: {'max': '1100px'},
      md: {'max': '999px'},
      sx: {'max': '900px'},
      sm: {'max': '800px'},
      ms: {'max': '670px'},
      xs: {'max': '450px'},
    },
  },
  plugins: [],
}

