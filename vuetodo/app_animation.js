const vm = new Vue({
	el: "#demo",
	data: {
		show: true
	}
});
new Vue({
	el: "#example-2",
	data: {
		show: true
	}
})
new Vue({
	el: "#example-3",
	data: {
		show: true
	}
})
new Vue({
	el: "#list-complete-demo",
	data: {
		items: [1,2,3,4,5,6,7,8,9],
		nextNum: 10
	},
	methods: {
		randomIndex: function () {
			return Math.floor(Math.random() * this.items.length)
		},
		add: function () {
			this.items.splice(this.randomIndex(), 0, this.nextNum++)
		},
		remove: function () {
			this.items.splice(this.randomIndex(), 1)
		},
	}
})
