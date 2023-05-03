/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./**/*.html'],
  darkMode: 'class',
  theme: {
    extend: {
      backgroundImage: {
        'header_img': "url('/public/img/bg-top-23_2.jpg')"
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

