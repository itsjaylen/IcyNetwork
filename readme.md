# Main App

## How to start

    docker compose up

# Information

## Bugs

- When composed a docker is not fetching the api's correctly (maybe a problem with the nuxt.config.ts and env variables)
- For the login fix the login error message system. When logging in properly the error message is still popping up

## Todo

- [ ] Fix DashboardSideBarScript.ts broken functions / convert DashboardsideBar script to typescript in its own file.
- [x] Break down the components into smaller components (e.g. api fetching)
- [ ] Add EKL logging
- [ ] Work on the logging system
- [ ] Better Design
- [ ] Fix the double sidebar menu
- [ ] Load everything for .env for easy access
- [ ] Dark, Light mode switch/ themes (Store with cookie maybe?)
- [ ] Design the default page by adding a footer, header, sidebar and navbar.
- [ ] Clean up the pages and store everything in the components folder
- [x] Covert everything to typescript and tailwinds
- [x] Remove the style and script code to put them in there own files
- [ ] Email server for email confirmation
- [ ] Add a forgot password system
- [ ] Add a 2FA system
- [ ] Profile Picture system / host CDN
- [ ] Add a R2 or AWS bucket for the images
- [ ] Add sms verification
- [ ] Localization
- [ ] Auth Middleware 
- [ ] Add user preferences in database
- [ ] Add css formatting for all devices (mobile, tablet, desktop)

## To implement

### Administrative

- [ ] user management system
- [ ] data base management
- [ ] analytics
- [ ] content management system
- [ ] moderation system
- [ ] settings and configuration
- [ ] back up and restore
- [ ] notifications and alert system
- [ ] audit logs
- [ ] user activity logs

### Profile Management

- [ ] change password
- [ ] change email
- [ ] change username
- [ ] change profile picture
- [ ] change theme
- [ ] change language (maybe)
- [ ] change timezone (maybe)
- [ ] change country (maybe)
- [ ] privacy settings
- [ ] 2FA/ Oauth Password Resetting

# Other scripts and resources to reference

```javascript
// Sets a cookie
const myCookieToken = useCookie("myCookieToken", {
  maxAge: 60 * 60 * 24 * 7,
  sameSite: "Strict",
});
```

- https://matrix-org.github.io/matrix-python-sdk/matrix_client.html
- ELK LOGGING https://www.youtube.com/watch?v=_EnyrFKF4K4
