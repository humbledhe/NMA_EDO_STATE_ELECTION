//import { Link } from "react-router-dom";
// Local modules
import Header from "../components/Header.jsx";

function LandingPage() {
    return (
        <>
            <header className="bg-[#0D3419] text-white">
                <Header />
                <div className="flex flex-col items-center py-[12rem]">
                    <p className="text-xl mb-[2em] text-[#D7B85A] bg-[#314122] border border-[#556C33] px-[3em] py-[10px] rounded-[35px]">
                        2026 MAIN ELECTION . EDO STATE CHAPTER
                    </p>
                    <p className="text-5xl text-[#F5F5F2] font-bold mb-[4px]">
                        YOUR VOTE.
                    </p>
                    <p className="text-5xl text-[#E2C45B] font-bold">
                        YOUR VOICE
                    </p>

                    <h2 className="text-3xl text-[#808080] font-bold mt-[1em]">
                        NIGERIAN MEDICAL ASSOCIATION
                    </h2>
                    <p className="text-3xl font-bold text-[#808080] my-[3em] w-[85%] text-center">
                        The NMA Edo State 2026 executive election is now open
                        for pre-registration. Only verified members may
                        participate. Cast your ballot securely online.
                    </p>

                    <div className="flex gap-[1em]">
                        <p className="bg-[#D4AF2A] text-[#1F2B1A] py-[1em] px-[3em] rounded-[20px] text-2xl font-bold">
                            Pre-register to vote
                        </p>
                        <p className="text-2xl py-[1em] px-[1.5em] rounded-[10px] border border-[#808080] font-bold">
                            How it works
                        </p>
                    </div>
                    <p className="text-2xl mt-[7em]">Voting opens in</p>
                </div>
            </header>
        </>
    );
}

export default LandingPage;
