<script lang="ts">
  export let num: number;
  export let letter: string;
</script>

<div>
  <button
    type="button"
    id={"sel_" + num.toString()}
    class="py-2 px-4 text-sm font-medium text-gray-200 bg-gray-700 border border-gray-600 hover:bg-gray-600 focus:bg-gray-600 focus:outline focus:outline-offset-2 focus:outline-red-700"
  >
    {num}
  </button>
  <br />
  {letter}
</div>
