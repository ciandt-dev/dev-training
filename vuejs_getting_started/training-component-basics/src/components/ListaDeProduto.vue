<template>
  <div>
    <h2>{{ titulo }}</h2>
    <ul>
      <li v-for="(produto, i) in lista" :key="i">
        <slot name="default" v-bind:produto="produto" v-bind:id="i">
          <div @click="cliqueNoProduto(produto, $event)">{{ produto.titulo }}</div>
        </slot>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'ListaDeProduto',
  props: {
    lista: Array,
    titulo: String
  },
  methods: {
    cliqueNoProduto (produto, event) {
      this.$emit('clique-no-produto', produto, event)
    }
  }
}
</script>
