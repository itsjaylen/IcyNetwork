import { defineComponent } from "vue";
import useLogin from "~/composables/AuthUtils/loginUtils";

export default defineComponent({
  setup() {
    const { email, password, errorMessage, login }: any = useLogin();

    return {
      email,
      password,
      errorMessage,
      login,
    };
  },
});
