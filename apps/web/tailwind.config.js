/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        surface: {
          DEFAULT: "#f4f4f5",
          card: "#ffffff",
          border: "#e4e4e7",
        },
        ink: {
          DEFAULT: "#18181b",
          muted: "#71717a",
        },
        accent: {
          DEFAULT: "#0f766e",
          fg: "#ffffff",
        },
      },
    },
  },
  plugins: [],
};
