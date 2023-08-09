import DashboardScript from "./DashboardScript";
import { useRouter } from "vue-router";

interface Setting {
  id: number;
  title: string;
  icon: string;
  action: () => void;
}

interface ComponentData {
  loggedIn: boolean;
  search: string;
  lightModeEnabled: boolean;
  settings: Setting[];
  user: string;
}

interface ComponentComputed extends ComponentData {
  filteredSettings: Setting[];
}

interface ComponentMethods {
  goToSettings: () => Promise<void>;
  goToAccount: () => Promise<void>;
  goToNotifications: () => Promise<void>;
  goToPrivacy: () => Promise<void>;
  goToLogout: () => void;
  toggleLightMode: () => void;
  goToMessages: () => Promise<void>;
  goToDashboard: () => Promise<void>;
  goToHome: () => Promise<void>;
  addNewItem: (id: number, title: string, icon: string, action: () => void) => void;
}

export default {
  ...(DashboardScript as Record<string, unknown>),
  name: "DashboardSideBar",
  data(): ComponentData {
    const router = useRouter();
    return {
      loggedIn: true,
      search: "",
      lightModeEnabled: false,
      settings: [] as Setting[],
      user: (DashboardScript.setup() as unknown as { user: string }).user,
    };
  },
  computed: {
    filteredSettings(this: ComponentComputed): Setting[] {
      const query = this.search.toLowerCase();
      return this.settings.filter((setting) =>
        setting.title.toLowerCase().includes(query)
      );
    },
  },
  methods: {
    async goToSettings(this: ComponentMethods): Promise<void> {
      await navigateTo("/settings");
    },
    async goToAccount(this: ComponentMethods): Promise<void> {
      await navigateTo("/account");
    },
    async goToNotifications(this: ComponentMethods): Promise<void> {
      await navigateTo("/notifications");
    },
    async goToPrivacy(this: ComponentMethods): Promise<void> {
      await navigateTo("/privacy");
    },
    goToLogout(this: ComponentMethods): void {
      // Perform logout logic here
    },
    toggleLightMode(this: ComponentData & ComponentMethods): void {
      this.lightModeEnabled = !this.lightModeEnabled;
      localStorage.setItem(
        "lightModeEnabled",
        JSON.stringify(this.lightModeEnabled)
      );
      if (this.lightModeEnabled) {
        // Light mode is enabled
        // Apply light mode styles
      } else {
        // Light mode is disabled
        // Apply default styles
      }
    },
    async goToMessages(this: ComponentMethods): Promise<void> {
      await navigateTo("/messages");
    },
    async goToDashboard(this: ComponentMethods): Promise<void> {
      await navigateTo("/dashboard");
    },
    async goToHome(this: ComponentMethods): Promise<void> {
      await navigateTo("/");
    },
    addNewItem(this: ComponentData & ComponentMethods, id: number, title: string, icon: string, action: () => void): void {
      this.settings.push({
        id,
        title,
        icon,
        action,
      });
    },
  },
  mounted() {
    const storedLightModeEnabled = localStorage.getItem("lightModeEnabled");
    if (storedLightModeEnabled !== null) {
      this.lightModeEnabled = JSON.parse(storedLightModeEnabled);
    }

    this.addNewItem(1, "Home", "mdi-home", this.goToHome);
    this.addNewItem(2, "Dashboard", "mdi-view-dashboard", this.goToDashboard);
    this.addNewItem(3, "Settings", "mdi-cog", this.goToSettings);
    this.addNewItem(4, "Account", "mdi-account", this.goToAccount);
    this.addNewItem(
      5,
      "Notifications",
      "mdi-bell-ring",
      this.goToNotifications
    );
  },
};
