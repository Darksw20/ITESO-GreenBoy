new Vue({
    el: "#app",
    data: {
        username: "",
        password: ""
    },
    mounted(){
        axios.defaults.xsrfCookieName = 'csrftoken'
        axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
    },
    methods:{
        login:function(){
            axios.post("webservices/signin",{
                user: this.username,
                passw: this.password
            })
            .then(resp=>{
                if(resp.data == 1){
                    window.location.href="http://localhost:8000/greenBoy/dash";
                }else{
                    alert("Usuario no existe")
                }
            })
        }
    }
})