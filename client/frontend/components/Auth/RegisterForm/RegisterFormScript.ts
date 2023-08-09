import useRegistration from "~/composables/AuthUtils/registerUtils";

export default {
  setup() {
    const {
      username,
      email,
      newPassword,
      confirmPassword,
      errorMessage,
      register,
    }  = useRegistration();

    return {
      username,
      email,
      newPassword,
      confirmPassword,
      errorMessage,
      register,
    };
  },
};
