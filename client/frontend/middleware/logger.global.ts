export default defineNuxtRouteMiddleware((to, from) => {


  // proper implementation
  const isLoggedIn = true;
  if (isLoggedIn) {
    console.log("User is logged in");
  } else {
    if (to.path !== "/login") {
      return navigateTo("/login");
    }
  }

  if (to.path === "/login") {
    // Skip redirection if already on the login page
    return;
  }
});
