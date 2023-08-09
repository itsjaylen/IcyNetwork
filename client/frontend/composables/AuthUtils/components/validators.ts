// validators.js
export function validatePasswordsMatch(
  newPassword: string,
  confirmPassword: string
) {
  if (newPassword !== confirmPassword) {
    throw new Error("Passwords do not match");
  }
}

export function validateEmailFormat(email: string) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email)) {
    throw new Error("Invalid email format");
  }
}

export function validateAndCacheResponse(responseData: any): void {
  try {
    JSON.parse(JSON.stringify(responseData)); // Validate the JSON
    const cachedData = {
      user: Object.freeze(responseData), // Make the user object read-only
      timestamp: Date.now(),
    };
    sessionStorage.setItem("cachedResponse", JSON.stringify(cachedData));
  } catch (error) {
    throw new Error(`Invalid JSON response: ${error}`);
  }
}
