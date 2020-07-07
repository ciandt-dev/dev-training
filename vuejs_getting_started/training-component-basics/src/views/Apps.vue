<template>
  <div class="apps">
    <button>Criar</button>

    <!-- <span v-show="descricaoDoProduto">{{ descricaoDoProduto }}</span> -->

    <lista-de-produto titulo="Meus Apps"
      :lista="apps"
      @clique-no-produto="mostrarDescricao"
    >
    <template v-slot="{ produto, id }">
      <div>
      Acertei {{ id }} miserávi: {{ produto.descricao }}
      </div>
    </template>
    </lista-de-produto>

    <lista-de-produto
      titulo="Minhas Promoções"
      :lista="promos"
      @clique-no-produto="mostrarDescricao"
    />
  </div>
</template>

<script>
import ListaDeProduto from '../components/ListaDeProduto'

export default {
  data: () => {
    return {
      produtos: [
        { tipo: 'app', titulo: 'Título 1', descricao: 'Descricao 1' },
        { tipo: 'app', titulo: 'Título 2', descricao: 'Descricao 2' },
        { tipo: 'app', titulo: 'Título 3', descricao: 'Descricao 3' },
        { tipo: 'promo', titulo: 'Promo 1', descricao: 'Descricao da Promo 1' },
        { tipo: 'promo', titulo: 'Promo 2', descricao: 'Descricao da Promo 2' },
        { tipo: 'promo', titulo: 'Promo 3', descricao: 'Descricao da Promo 3' }
      ],
      descricaoDoProduto: ''
    }
  },
  computed: {
    apps () {
      return this.produtos.filter(p => p.tipo === 'app')
    },
    promos () {
      return this.produtos.filter(p => p.tipo === 'promo')
    }
  },
  methods: {
    mostrarDescricao (produto, event) {
      this.descricaoDoProduto = produto.descricao
      console.log(event)
    }
  },
  components: {
    ListaDeProduto
  }
}
</script>
