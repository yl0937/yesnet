<template>
 <div class="container-fluid">
  <div class="row">
    <nav class="col-md-2 d-none d-md-block bg-light sidebar">
      <div class="sidebar-sticky">
        <ul class="nav flex-column">
          <li class="nav-item">
            <a class="nav-link active" href="/">
              <span data-feather="home"></span>
              DashBoard <span class="sr-only">(current)</span>
            </a>
          </li>
          <li class="nav-item">
              <h6 class="sidebar-heading d-flex justify-content-between align-items-center px-3 mt-4 mb-1 text-muted">
          <span>DApps</span>
          </h6>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/DAppsUpload">
              DApps Upload
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/DAppsList">
              DApps List
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/DeployedDApps">
              Deployed DApps
            </router-link>
          </li>
        </ul>

        <h6 class="sidebar-heading d-flex justify-content-between align-items-center px-3 mt-4 mb-1 text-muted">
          <span>WATCHERS</span>
        </h6>
        <ul class="nav flex-column mb-2">
          <li class="nav-item">
            <router-link class="nav-link" to="/WatchBlock">
              Watch Block
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/WatchTX">
              Watch TX
            </router-link>
          </li>
        </ul>
        <h6 class="sidebar-heading d-flex justify-content-between align-items-center px-3 mt-4 mb-1 text-muted">
          <span>Login</span>
        </h6>
          <ul class="nav flex-column mb-2">
            <li class="nav-item">
          <router-link class="nav-link" to="/login">
              Login
            </router-link>
          </li>
            </ul>
      </div>
    </nav>
   </div>
   </div>
</template>
<style scoped>
.sidebar {
  position: fixed;
  top: 50px;
  bottom: 0;
  left: 0;
  z-index: 100; /* Behind the navbar */
  padding: 48px 0 0; /* Height of navbar */
  box-shadow: inset -1px 0 0 rgba(0, 0, 0, .1);
}

.sidebar-sticky {
  position: relative;
  top: 0;
  height: calc(100vh - 48px);
  padding-top: .5rem;
  overflow-x: hidden;
  overflow-y: auto; /* Scrollable contents if viewport is shorter than content. */
}

@supports ((position: -webkit-sticky) or (position: sticky)) {
  .sidebar-sticky {
    position: -webkit-sticky;
    position: sticky;
  }
}

.sidebar .nav-link {
  font-weight: 500;
  color: #333;
}

.sidebar .nav-link .feather {
  margin-right: 4px;
  color: #999;
}

.sidebar .nav-link.active {
  color: #007bff;
}

.sidebar .nav-link:hover .feather,
.sidebar .nav-link.active .feather {
  color: inherit;
}

.sidebar-heading {
  font-size: .75rem;
  text-transform: uppercase;
}
</style>
