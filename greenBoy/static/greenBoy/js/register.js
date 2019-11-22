new Vue({
    el: "#app",
    data: {
        username: "",
        password: "",
        vpassword: "",
        email: ""
    },
    mounted(){
        axios.defaults.xsrfCookieName = 'csrftoken'
        axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
    },
    methods:{
        register:function(){
            if(this.password===this.vpassword){
                axios.post("webservices/register",{
                    user: this.username,
                    passw: this.password,
                    email: this.email
                })
                .then(resp=>{
                    if(resp.data.message === "USER_REGISTRED"){
                        window.location.href = "http://localhost:8000/greenBoy/dash";
                    }else if(resp.data.message === "USER_ALREADY_EXIST"){
                        alert("Usuario ya existe")
                    }else{
                        alert("ERROR")
                    }
                })
            }else{
                alert("Verifique su contraseña")
            }
        }
    }
})