interface LoginResponse {
  access_token?: string;
  error?: string;
}

export async function performLoginRequest(
  csrfToken: string,
  email: string,
  password: string,
  apiBase: string
): Promise<LoginResponse> {
  const response = await $fetch("/api/login", {
    baseURL: apiBase,
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRF-TOKEN": csrfToken,
    },
    body: JSON.stringify({
      email,
      password,
    }),
    credentials: "include",
  });
  return response as LoginResponse;
}

export async function sendRegistrationRequest(
  username: string,
  email: string,
  password: string,
  csrfTokenValue: string,
  apiBase: string
): Promise<any> {
  const apiRequestPromise = $fetch("/api/register", {
    baseURL: apiBase,
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRF-TOKEN": csrfTokenValue,
    },
    body: JSON.stringify({
      username,
      email,
      password,
    }),
  });

  const timeoutPromise = new Promise((_, reject) => {
    setTimeout(() => {
      reject(new Error("Request timeout"));
    }, 10000);
  });

  const response = await Promise.race([apiRequestPromise, timeoutPromise]);
  return response;
}

export async function fetchProtectedData(
  apiBase: string,
  csrfToken: string
): Promise<any> {
  const response: any = await useFetch(`${apiBase}/api/protected`, {
    headers: {
      "Content-Type": "application/json",
      "X-CSRF-TOKEN": csrfToken,
    },
    credentials: "include",
  });

  return response.data._rawValue.user;
}
