new Vue({
    el: "#app",
    data: {
        username: "",
        password: ""
    },
    mounted(){},
    methods:{
        login:function(){
            console.log("Se enviaron"+this.username+" "+this.password)

            axios.post("webservices/signin",{
                user: this.username,
                passw: this.password
            }).then(resp=>{
                switch(resp.data.response){

                    default:
                        console.log("Se enviaron"+this.username+" "+this.password)
                       // window.location = ""
                }
            })
        }
    }
})