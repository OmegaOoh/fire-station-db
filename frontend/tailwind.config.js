/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./public/index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
  daisyui: {
    theme: ['light', 'dark'],
    darkTheme: 'dark',
    base: true,
    styled: true,
    logs: true,
    themeRoot: ":root"
  }
}

