import { navbar } from "vuepress-theme-hope";

export const zhNavbar = navbar([
  "/",
  {
    text: "通史",
    icon: "material-symbols:globe-asia",
    link: "/global/",
  },
  { text: "列传", icon: "material-symbols:docs-outline", link: "/personal/" },
  {
    text: "往事",
    icon: "material-symbols:history-rounded",
    link: "/old/",
  },
]);
