export default defineComponent({
  setup() {
    const { loading, error, user, fetchUserData } = useUserData();

    // Call the fetchUserData function to trigger the data fetching
    fetchUserData();


    return {
      loading,
      error,
      user,
    };
  },
});
