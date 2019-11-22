
new Vue({
    el: "#app",
    delimiters: ['[[', ']]'],
    data: {
        invArray: [],
        invSelected: "",
        name: "",
        invName: "",
        tempMax: null,
        tempMin: null,
        humMax: null,
        humMin: null,
        editInvName: ""
    },
    mounted() {
        axios.defaults.xsrfCookieName = 'csrftoken'
        axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
        this.initializate()
    },
    methods: {
        initializate: function () {
            axios.get("webservices/getInfoGreen")
            .then(resp => {
                this.name = resp.data.user
                if (resp.data.greenData.length > 0) {
                    this.invArray = resp.data.greenData
                    this.invSelected = this.invArray[0].greenName
                    this.tempMax = resp.data.greenData[0].temp_max
                    this.tempMin = resp.data.greenData[0].temp_min
                    this.humMax = resp.data.greenData[0].hum_max
                    this.humMin = resp.data.greenData[0].hum_min
                    this.editInvName = resp.data.greenData[0].greenName
                }
                return resp.data.greenData.length;
            })
            .then(resp=>{
                if (resp != 0) {
                    var ctx = document.getElementById('myChart').getContext('2d');
                    var myChart = new Chart(ctx, {
                        type: 'line',
                        data: {
                            labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
                            datasets: [{
                                label: '# of Votes',
                                data: [12, 19, 3, 5, 2, 3],
                                backgroundColor: [
                                    'rgba(255, 99, 132, 0.2)',
                                    'rgba(54, 162, 235, 0.2)',
                                    'rgba(255, 206, 86, 0.2)',
                                    'rgba(75, 192, 192, 0.2)',
                                    'rgba(153, 102, 255, 0.2)',
                                    'rgba(255, 159, 64, 0.2)'
                                ],
                                borderColor: [
                                    'rgba(255, 99, 132, 1)',
                                    'rgba(54, 162, 235, 1)',
                                    'rgba(255, 206, 86, 1)',
                                    'rgba(75, 192, 192, 1)',
                                    'rgba(153, 102, 255, 1)',
                                    'rgba(255, 159, 64, 1)'
                                ],
                                borderWidth: 1
                            }]
                        },
                        options: {
                            scales: {
                                yAxes: [{
                                    ticks: {
                                        beginAtZero: true
                                    }
                                }]
                            }
                        }
                    });
                }
            })
        },
        newGreen: function(){
            axios.post('webservices/newGreen',{ greenName: this.invName })
            .then(resp=>{
                location.reload();
            })
        },
        delGreen: function(){
            axios.post('webservices/delGreen',{ greenName: this.invSelected })
            .then(resp=>{
                location.reload();
            })
        },
        saveData: function(){
            axios.post('webservices/setDataGreen',{
                temp_max: this.tempMax,
                temp_min: this.tempMin,
                hum_max: this.humMax,
                hum_min: this.humMin,
                nameInv: this.editInvName,
                greenName: this.invSelected
            })
            .then(resp=>{
                if(resp.data.message = "GREEN_UPDATED"){
                    alert("Datos cambiados con exito")
                    location.reload();
                }else{
                    alert("ERROR")
                }
            })
        }
    }
})