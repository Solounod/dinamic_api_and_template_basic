import { Footer } from "../footer/Footer";
import { NavbarBase } from "../header/NavbarBase"


export function LayoutFull({children}) {

    return (
        <> 
            <NavbarBase/>
                {children}
            <Footer/>
        </>
    )
} 