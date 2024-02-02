import { useNavigate} from "react-router-dom"
export function RegisterLoginBar() {
    const navigate = useNavigate()
    return (
        <div>
            <p>
                <a onClick={() => {navigate('/Register')}}>Register/</a>
                <a onClick={() => {navigate('/Login')}}>Login</a>
            </p>
        </div>
    )
}