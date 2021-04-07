<template>
	<div class="openstreetmap">
		<link rel="preconnect" href="https://fonts.gstatic.com">
		<link href="https://fonts.googleapis.com/css2?family=Pacifico&display=swap" rel="stylesheet">
		<p class="title">Stimap</p>
		<button class="done" @click="isClickedB=true">Selesai membuat graf</button>
        <button class="send" @click="sendList()">OK!</button>
		<p v-if="counterSelected<=2 && isClickedB==true">Pilih 2 titik!</p>
		<p v-if="counterSelected>2">Kamu sudah memilih 2 titik</p>
        <p v-if="cost!=0">Jarak : {{cost}} km</p>
        <p v-if="isFound==false">Kedua titik tidak berhubungan</p>
		<l-map style="height: 450px" :zoom="zoom" :center="center"  @click="onMapClick">
			<l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
			<l-marker v-for="marker,index in markers" :lat-lng="marker" :icon="iconNormal" v-bind:key="index" @click="markerClick"></l-marker>
			<l-polyline v-for="elem,index in nodes" :lat-lngs="elem[0]" :color="elem[1]" v-bind:key="index" ></l-polyline>
			<l-polyline v-for="e,i in astar" :lat-lngs="e[0]" :color="e[1]" v-bind:key="i"></l-polyline>
		</l-map>
	</div>
</template>
<style type="text/css">
@import "https://unpkg.com/leaflet-geosearch@2.6.0/assets/css/leaflet.css";

#app{
	margin-top:0px !important;
}
.title{
	font-family:'Pacifico', cursive;
	font-size:60px;
	margin-bottom:20px;
	margin-top:0px;
}
.leaflet-popup-close-button {
	display: none; 
}
.done{
	margin-right:7px;
	margin-bottom:15px;
	background-color:#43cacc;
	color : white;
	padding:10px;
	border : none;
	border-radius:5px;
	font-size:18px;
	cursor:pointer;
}

.send{
	color : white;
	background-color:#db932e;
	padding:10px;
	border : none;
	border-radius:5px;
	font-size:18px;
	cursor:pointer;
}

</style>
<script>
	import {LMap, LTileLayer, LMarker, LPolyline} from 'vue2-leaflet';
	import L from 'leaflet'
	import 'leaflet/dist/leaflet.css'
    import json from '../node.json'
	import { OpenStreetMapProvider } from 'leaflet-geosearch';

	delete L.Icon.Default.prototype._getIconUrl

	export default {
		name: 'Openstreetmap',
		components: {
			LMap,
			LTileLayer,
			LMarker,
			LPolyline
		},
		data: () => ({
			isClickedB:false,
			zoom:20,
			center: L.latLng(-6.890364997716474, 107.61034998436544),
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
			iconNormal: L.icon({
                iconUrl: "https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-blue.png",
                iconAnchor: [12, 41],
                popupAnchor: [0, -41]
            }),
			iconAsal: L.icon({
                iconUrl: "https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-red.png",
                iconAnchor: [12, 41],
                popupAnchor: [0, -41]
            }),
			node:[],
			nodes:[],
			markers:[],
			selected:[],
            edges:[],
            astar:[],
            cost:0,
            isFound:null,
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
						this.nodes.push([this.node, "red"]);
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
						this.nodes.push([this.node, "red"]);
						console.log(this.nodes)
						this.node=[];
					}
				}
				else{
					if (this.counterSelected < 2){
						this.selected.push([e.latlng.lat,e.latlng.lng]);
                        e.target.setIcon(this.iconAsal);                        
					}
                    this.counterSelected=this.counterSelected+1;
				}
			},

            sendList() {
				const stripNodes = this.nodes.map(e => e[0])
                var nodes_json = JSON.stringify({"edges" : stripNodes, "nodes":this.markers, "selected":this.selected})
                
                fetch('http://127.0.0.1:5000/', {
                    method: 'POST',
                    body: nodes_json,
                    headers: {
                    'Accept': 'application/json, text/plain, */*',
                    'Content-Type': 'application/json'
                    }
                }).then (response => {
                    response.json().then(data => {
						this.astar=data[0].map(e => [e,"blue"]);
                        this.cost = data[2];
                        this.isFound = data[1];
                        console.log(this.cost)
					});
                }).catch(
                    error => console.error(error)
                );
            }
		}
	}
</script>