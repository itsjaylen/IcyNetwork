import { fetchProtectedData } from "./AuthUtils/components/api";
import { validateAndCacheResponse } from "./AuthUtils/components/validators";
import CsrfTokenResponse from "./CsrfTokenResponse";

export function useUserData() {
  const loading = ref(true);
  const error = ref(null);
  const user = ref(null);

  async function fetchUserData() {
    try {
      const config = useRuntimeConfig();
      const csrfTokenResponse = (await fetchCsrfToken()) as CsrfTokenResponse;
      const csrfToken = csrfTokenResponse.csrf_token;

      const cachedResponse = sessionStorage.getItem("cachedResponse");
      if (cachedResponse) {
        const parsedResponse = JSON.parse(cachedResponse);
        const expirationTime = parsedResponse.timestamp + 10 * 60 * 1000; // 10 minutes
        if (Date.now() < expirationTime) {
          user.value = Object.freeze(parsedResponse.user); // Make the cached user object read-only
          loading.value = false;
          return;
        }
      }

      const responseData = await fetchProtectedData(
        config.public.apiBase,
        csrfToken
      );

      validateAndCacheResponse(responseData);

      loading.value = false;
      user.value = Object.freeze(responseData);
    } catch (error: any) {
      loading.value = false;
      error.value = error.message;
    }
  }

  return {
    loading,
    error,
    user,
    fetchUserData,
  };
}
