import InputComponent from "../InputComponent/InputComponent";
import "../InputComponent/InputComponent.css"

function PanelComponent() {
    return (
        <>
            <div className="panel-wrapper">
                <InputComponent />
            </div>
        </>
    )
}

export default PanelComponent;