import { performLoginRequest } from "./components/api";
import { validateEmailFormat } from "./components/validators";

interface LoginData {
  email: Ref<string>;
  password: Ref<string>;
  errorMessage: Ref<string | undefined>;
}

interface CsrfTokenResponse {
  csrf_token: string;
}

interface LoginResponse {
  access_token?: string;
  error?: string;
}

export default function useLogin(): LoginData {
  const email = ref("");
  const password = ref("");
  const errorMessage = ref<string | undefined>(undefined);
  const config = useRuntimeConfig();

  async function login(): Promise<void> {
    try {
      const isValidEmail: boolean | void = validateEmailFormat(email.value);
      if (isValidEmail === false) {
        errorMessage.value = "Invalid email format";
        return;
      }

      const csrfToken = await getCsrfToken();
      const response = await performLoginRequest(
        csrfToken,
        email.value,
        password.value,
        config.public.apiBase
      );

      if (response.access_token) {
        await navigateTo("/dashboard");
      }

      if (response.error) {
        errorMessage.value = response.error;
      }
    } catch (error) {
      console.error(error);
      errorMessage.value = "Login failed. Please try again.";
    }
  }

  async function getCsrfToken(): Promise<string> {
    const csrfTokenResponse = await fetchCsrfToken();
    return (csrfTokenResponse as CsrfTokenResponse).csrf_token;
  }

  function validateEmailFormat(emailValue: string): boolean {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(emailValue);
  }

  return {
    email,
    password,
    errorMessage,
    login,
  } as unknown as LoginData;
}
