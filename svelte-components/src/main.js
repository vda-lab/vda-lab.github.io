import Airports from './Airports.svelte';
import Animation1 from './Animation1.svelte';
import Animation2 from './Animation2.svelte';
import Iris from './Iris.svelte';

new Airports({
	target: document.querySelector('#svelte-airports'),
});
new Animation1({
	target: document.querySelector('#svelte-animation1'),
});
new Animation2({
	target: document.querySelector('#svelte-animation2'),
});
new Iris({
	target: document.querySelector('#svelte-iris'),
})