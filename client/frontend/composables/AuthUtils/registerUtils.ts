import { validatePasswordsMatch, validateEmailFormat } from "./components/validators";
import { sendRegistrationRequest } from "./components/api";

interface RegistrationData {
  username: string;
  email: string;
  newPassword: string;
  confirmPassword: string;
  errorMessage: string;
  register: () => Promise<void>; // Define the register function type
}


export default function useRegistration() {
  const username = ref("");
  const email = ref("");
  const newPassword = ref("");
  const confirmPassword = ref("");
  const errorMessage = ref("");
  const config = useRuntimeConfig();

  async function validateAndRegister() {
    try {
      validateInputs();
      await performRegistration();
    } catch (error) {
      handleError(error as Error);
    }
  }

  function validateInputs() {
    validatePasswordsMatch(newPassword.value, confirmPassword.value);
    validateEmailFormat(email.value);
  }

  async function performRegistration() {
    const csrfTokenResponse = await fetchCsrfToken();
    const csrfTokenValue: string = csrfTokenResponse as string;

    const response = await sendRegistrationRequest(
      username.value,
      email.value,
      confirmPassword.value,
      csrfTokenValue,
      config.public.apiBase
    );

    if (response) {
      handleSuccess();
    } else {
      handleFailure(response);
    }
  }

  function handleSuccess() {
    // Registration successful
    // For example, display a success message or redirect to a confirmation page
    navigateTo("/login");
  }

  function handleFailure(response: any) {
    const errorData = response;
    console.error(errorData);
    errorMessage.value = errorData.error;
  }

  function handleError(error: Error) {
    console.error(error);
    if (error.message === "Request timeout") {
      errorMessage.value = "Server did not respond within 10 seconds";
    } else {
      errorMessage.value =
        "Registration failed. Please try again with a different email.";
    }
  }

  return {
      username,
      email,
      newPassword,
      confirmPassword,
      errorMessage,
      register: validateAndRegister,
  } as unknown as RegistrationData;
}
