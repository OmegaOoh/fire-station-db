<template>
  <div class="absolute z-20 px-2 top-0 right-1">
    <div class="dropdown dropdown-end">
      <div tabindex="0" role="button" class="btn btn-neutral m-1">Navigate</div>
      <ul tabindex="0" class="dropdown-content menu bg-neutral rounded-box z-[1] w-52 p-2 shadow">
    <li><RouterLink to="/"> Home </RouterLink></li>
    <li><RouterLink to="/find"> Record Finder </RouterLink></li>
    <li><RouterLink to="/station"> Station </RouterLink></li>
    <li><RouterLink to="/staff"> Staff List </RouterLink></li>
  </ul>
</div>
  </div>
    <router-view class="mt-4 mx-4"/>
</template>

