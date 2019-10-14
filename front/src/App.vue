<template>
  <div id="app">
    <section class="hero is-primary">
      <div class="hero-head">
        <nav class="navbar">
          <div class="container">
            <div id="navbarMenuHeroB" class="navbar-menu">
              <div class="navbar-end">
                <span class="navbar-item">
                  <a class="button is-primary is-inverted">
                    <span>Configuration</span>
                  </a>
                </span>
              </div>
            </div>
          </div>
        </nav>
      </div>
    </section>
    <br />
    <div class="container">
      <Dashboard></Dashboard>
    </div>
  </div>
</template>

<script>
import Dashboard from "./components/Dashboard.vue";

export default {
  name: "app",
  components: {
    Dashboard
  }
};
</script>

