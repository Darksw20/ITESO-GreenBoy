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
                if(resp.data.message == "USER_AUTHENTICATED"){
                    window.location.href="http://localhost:8000/greenBoy/dash";
                }else if(resp.data.message == "INVALID_USER"){
                    alert("Usuario no existe")
                }else{
                    alert("ERROR")
                }
            })
        }
    }
})