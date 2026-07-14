// Local modules
import logo from "../img/logo.png";

function DashBoard() {
    return (
        <>
            <header className="bg-gradient-to-r from-[#0D5A27] to-[#1B7A3A] py-[8em] relative overflow-hidden">
                <div className="absolute -top-32 right-[-150px] w-[500px] h-[500px] rounded-full bg-white/5">
                    {" "}
                </div>

                <div className="absolute bottom-[-120px] left-[250px] w-[450px] h-[450px] rounded-full bg-white/5"></div>

                <div className="relative z-10 ml-[3em] flex flex-col justify-start">
                    <div>
                        <img className="w-[200px] mb-[1em]" src={logo} />
                    </div>
                    <h1 className="text-white text-5xl font-bold mb-[0.5em]">
                        NMA EDO STATE ELECTION
                    </h1>
                    <p className="text-3xl text-[#f5f5f274]">
                        NIGERIAN MEDICAL ASSOCIATION &#8226; MAIN ELECTION
                        &#8226; 2026
                    </p>
                    <p className="mt-[3em] text-[#E0C25A] text-2xl bg-[#4A682E] border border-[#7B8740] w-[11em] text-center py-[0.5em] rounded-[30px] font-bold">
                        <span className="mr-[5px]">&#10003;</span>RESULTS FINAL
                    </p>
                </div>
            </header>

            <main>
                <section className="flex text-3xl">
                    <div className="text-center border border-[#E5E7EB] flex-1 py-[1em]">
                        <p className="font-bold text-5xl text-[#0F5A2E]">6</p>
                        <p className="text-[#80808069] font-bold">POSITIONS</p>
                    </div>
                    <div className="text-center border border-[#E5E7EB] flex-1 py-[1em]">
                        <p className="font-bold text-5xl text-[#0F5A2E]">6</p>
                        <p className="text-[#80808069] font-bold">
                            TOTAL VOTERS
                        </p>
                    </div>
                    <div className="text-center border border-[#E5E7EB] flex-1 py-[1em]">
                        <p className="font-bold text-5xl text-[#0F5A2E]">6</p>
                        <p className="text-[#80808069] font-bold">CANDIDATES</p>
                    </div>
                    <div className="text-center border border-[#E5E7EB] flex-1 py-[1em]">
                        <p className="font-bold text-5xl text-[#0F5A2E]">6</p>
                        <p className="text-[#80808069] font-bold">COUNTED</p>
                    </div>
                </section>
            </main>
        </>
    );
}

export default DashBoard;
