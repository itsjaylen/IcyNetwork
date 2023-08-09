export async function fetchCsrfToken() {
  const config = useRuntimeConfig();

  
  const csrfTokenResponse = await $fetch("/api/csrf-token", {
    baseURL: config.public.apiBase, // Replace with your API base URL
    method: "GET",
  });


  return csrfTokenResponse;
}
