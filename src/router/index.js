import { createRouter, createWebHistory } from "vue-router";

// Import all views including those in subdirectories
const views = import.meta.glob('../views/**/*.vue')

const generateRoute = (path) => {
  // Extract name from path, removing .vue extension
  const name = path.match(/\.\.\/views\/(.*)\.vue$/)[1].toLowerCase()
  const segments = name.split('/')
  
  return {
    // Create path based on file location
    path: segments[segments.length - 1] === 'home' 
      ? '/' 
      : `/${segments.join('/')}`,
    name: segments[segments.length - 1],
    component: views[path]
  }
}

const routes = Object.keys(views).map(generateRoute)

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
});

export default router;