<template>	
	<div class="openstreetmap">
		<button class="done" @click="isClickedB=true">"udahan bikin graf"</button>
        <button class="send" @click="sendList()">OK!</button>
		<p v-if="counterSelected>2">Kamu sudah memilih 2 titik</p>
		<l-map style="height: 550px" :zoom="zoom" :center="center"  @click="onMapClick">
			<l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
			<l-marker v-for="marker,index in markers" :lat-lng="marker" v-bind:key="index" @click="markerClick"></l-marker>
			<l-polyline v-for="elem,index in nodes" :lat-lngs="nodes" v-bind:key="index"></l-polyline>
			<l-geosearch id="geosearch" :options="geosearchOptions"></l-geosearch>
		</l-map>
	</div>
</template>
<style type="text/css">
@import "https://unpkg.com/leaflet-geosearch@2.6.0/assets/css/leaflet.css";
.leaflet-popup-close-button {
	display: none; 
}
</style>
<script>
	import {LMap, LTileLayer, LMarker, LPolyline} from 'vue2-leaflet';
	import L from 'leaflet'
	import 'leaflet/dist/leaflet.css'
    import json from '../node.json'
	import { OpenStreetMapProvider } from 'leaflet-geosearch';
	import LGeosearch from "vue2-leaflet-geosearch";
    //import axios from 'axios';

	delete L.Icon.Default.prototype._getIconUrl
	L.Icon.Default.imagePath = ''
	L.Icon.Default.mergeOptions({
		iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
		iconUrl: require('leaflet/dist/images/marker-icon.png'),
		shadowUrl: require('leaflet/dist/images/marker-shadow.png')
	})
	export default {
		name: 'Openstreetmap',
		components: {
			LMap,
			LTileLayer,
			LGeosearch,
			LMarker,
			LPolyline
		},
		data: () => ({
			isClickedB:false,
			zoom:6,
			center: L.latLng(45.912944,24.224854),
			url:'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
			attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
			'<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
			'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
			id: 'mapbox/streets-v11',
			myJson : json,
			newLoc: '',
			newLt : 0, 
			newLng : 0, 
			counter : 0,
			counterSelected : 0,
			icon: L.icon({iconUrl: "null",}),
			node:[],
			nodes:[],
			markers:[],
			selected:[],
            edges:[],
			geosearchOptions: { // Important part Here
				provider: new OpenStreetMapProvider(),
			},
		}),
		mounted ()  {
			
			this.$nextTick(() => {
				this.$refs.marker.mapObject.openPopup();
			});
			this.newLoc = this.myJson[0].nama
			this.newLt = this.myJson[0].pos[0]
			this.newLng = this.myJson[0].pos[1]
			console.log(this.isClickedB)
		},
		methods: {
			onMapClick(e) {
				
				if (this.isClickedB==false){
					this.markers.push([e.latlng.lat, e.latlng.lng]);
					console.log(this.markers);
					this.counter=this.counter+1
					if (this.counter%2!=0){
						this.node.push([e.latlng.lat,e.latlng.lng]);
					}
					
					else if (this.counter%2==0){
						this.node.push([e.latlng.lat,e.latlng.lng]);
						this.nodes.push(this.node);
						this.node=[];
						
					}
				}
			},

			markerClick(e) {
				if (this.isClickedB==false){
					this.counter=this.counter+1
					if (this.counter%2!=0){
						this.node.push([e.latlng.lat,e.latlng.lng]);
					}
					
					else if (this.counter%2==0){
						this.node.push([e.latlng.lat,e.latlng.lng]);
						this.nodes.push(this.node);
						this.node=[];
					}
				}
				else{
					if (this.counterSelected <= 2){
						this.selected.push([e.latlng.lat,e.latlng.lng]);
						this.counterSelected=this.counterSelected+1;
					}
				}
			},

            sendList() {                
                var nodes_json = JSON.stringify({"edges" : this.nodes, "nodes":this.markers})
                
                fetch('http://127.0.0.1:5000/', {
                    method: 'POST',
                    body: nodes_json,
                    headers: {
                    'Accept': 'application/json, text/plain, */*',
                    'Content-Type': 'application/json'
                    }
                }).then(
                    resp => console.log(resp)
                ).catch(
                    error => console.error(error)
                );
            }
		}
	}
</script>