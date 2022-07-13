import pytest
from project import get_chesscom_archive, get_pgn_gamelength, get_total_length


def test_get_chesscom_archive():
    # This username and dates are used in the examples of the Chess.com API.
    # https://www.chess.com/news/view/published-data-api#pubapi-endpoint-games-archive
    username = "erik"
    year = "2019"
    month = "10"

    # Asserts that the function returns a dictionary.
    assert type(get_chesscom_archive(username, year, month)) == dict

    # Asserts that the program exits with incorrect username or date input
    with pytest.raises(SystemExit) as exit:
        get_chesscom_archive("davidmalanlovesducks", "", "")
    assert exit.type == SystemExit
    assert exit.value.code == "ERROR: 0"


def test_get_pgn_gamelength():
    # Just a chess.com PGN from a random recent game by a chess professional player.
    sample_pgn = '[Event "Live Chess"]\n[Site "Chess.com"]\n[Date "2022.07.05"]\n[Round "-"]\n[White "Hikaru"]\n[Black "Jospem"]\n[Result "0-1"]\n[CurrentPosition "2R5/1p4pk/3B1pp1/8/1P1n1P1P/6r1/4p3/5K2 w - -"]\n[Timezone "UTC"]\n[ECO "A04"]\n[ECOUrl "https://www.chess.com/openings/Reti-Opening-Sicilian-Invitation"]\n[UTCDate "2022.07.05"]\n[UTCTime "14:42:41"]\n[WhiteElo "3151"]\n[BlackElo "3016"]\n[TimeControl "180"]\n[Termination "Jospem won by resignation"]\n[StartTime "14:42:41"]\n[EndDate "2022.07.05"]\n[EndTime "14:47:25"]\n[Link "https://www.chess.com/game/live/50771333205"]\n\n1. Nf3 {[%clk 0:03:00]} 1... c5 {[%clk 0:03:00]} 2. b3 {[%clk 0:02:59.6]} 2... Nc6 {[%clk 0:02:59.3]} 3. Bb2 {[%clk 0:02:59.3]} 3... d5 {[%clk 0:02:58]} 4. e3 {[%clk 0:02:57.2]} 4... a6 {[%clk 0:02:57.6]} 5. d4 {[%clk 0:02:56.4]} 5... cxd4 {[%clk 0:02:57.5]} 6. exd4 {[%clk 0:02:55.7]} 6... Nf6 {[%clk 0:02:55.1]} 7. Bd3 {[%clk 0:02:55.2]} 7... Bg4 {[%clk 0:02:53.9]} 8. Nbd2 {[%clk 0:02:54.6]} 8... e6 {[%clk 0:02:53.3]} 9. a3 {[%clk 0:02:53.6]} 9... Bd6 {[%clk 0:02:51.6]} 10. h3 {[%clk 0:02:53.2]} 10... Bh5 {[%clk 0:02:50.2]} 11. O-O {[%clk 0:02:53]} 11... Bg6 {[%clk 0:02:49.8]} 12. Bxg6 {[%clk 0:02:51.4]} 12... hxg6 {[%clk 0:02:49.7]} 13. Re1 {[%clk 0:02:50.6]} 13... O-O {[%clk 0:02:48.9]} 14. c4 {[%clk 0:02:49.9]} 14... Re8 {[%clk 0:02:36.1]} 15. Ne5 {[%clk 0:02:47.1]} 15... Bxe5 {[%clk 0:02:28.4]} 16. dxe5 {[%clk 0:02:43.4]} 16... Nd7 {[%clk 0:02:28]} 17. cxd5 {[%clk 0:02:38.5]} 17... exd5 {[%clk 0:02:27.9]} 18. Nf3 {[%clk 0:02:36.2]} 18... Nc5 {[%clk 0:02:27.1]} 19. b4 {[%clk 0:02:35.1]} 19... Ne6 {[%clk 0:02:25.3]} 20. Qb3 {[%clk 0:02:34.7]} 20... Qd7 {[%clk 0:02:21.7]} 21. Rad1 {[%clk 0:02:34.4]} 21... Rad8 {[%clk 0:02:20.8]} 22. Rd2 {[%clk 0:02:34]} 22... d4 {[%clk 0:02:19.1]} 23. Red1 {[%clk 0:02:33.4]} 23... Qc7 {[%clk 0:02:17]} 24. Re1 {[%clk 0:02:29.9]} 24... Rd7 {[%clk 0:02:13.8]} 25. h4 {[%clk 0:02:27.6]} 25... Red8 {[%clk 0:02:09.5]} 26. g3 {[%clk 0:02:26.8]} 26... Rd5 {[%clk 0:02:08.4]} 27. Rde2 {[%clk 0:02:12.6]} 27... Qe7 {[%clk 0:01:56]} 28. Rd1 {[%clk 0:02:00.9]} 28... Rb5 {[%clk 0:01:50.5]} 29. Qd3 {[%clk 0:01:58.9]} 29... Rbd5 {[%clk 0:01:48.3]} 30. Rc1 {[%clk 0:01:52]} 30... Qd7 {[%clk 0:01:44.6]} 31. Rc4 {[%clk 0:01:47.4]} 31... a5 {[%clk 0:01:39.2]} 32. Rec2 {[%clk 0:01:38.8]} 32... axb4 {[%clk 0:01:36.3]} 33. axb4 {[%clk 0:01:37.8]} 33... Nxe5 {[%clk 0:01:35.5]} 34. Nxe5 {[%clk 0:01:37.2]} 34... Rxe5 {[%clk 0:01:35.4]} 35. Rd2 {[%clk 0:01:34.5]} 35... Re1+ {[%clk 0:01:33.5]} 36. Kh2 {[%clk 0:01:25.7]} 36... Qd5 {[%clk 0:01:32.8]} 37. f3 {[%clk 0:01:25.1]} 37... Re3 {[%clk 0:01:18.5]} 38. Qxe3 {[%clk 0:01:24.4]} 38... dxe3 {[%clk 0:01:18.4]} 39. Rxd5 {[%clk 0:01:24.3]} 39... Rxd5 {[%clk 0:01:18]} 40. Bc3 {[%clk 0:01:23.6]} 40... Rd2+ {[%clk 0:01:05.9]} 41. Kg1 {[%clk 0:01:19.5]} 41... Rc2 {[%clk 0:01:00.4]} 42. Kf1 {[%clk 0:01:17.8]} 42... Kh7 {[%clk 0:00:58]} 43. Ke1 {[%clk 0:01:14.2]} 43... Rf2 {[%clk 0:00:52.4]} 44. f4 {[%clk 0:01:07.9]} 44... Rg2 {[%clk 0:00:51.8]} 45. Be5 {[%clk 0:01:07]} 45... Rxg3 {[%clk 0:00:48.6]} 46. Rc8 {[%clk 0:01:04.7]} 46... f6 {[%clk 0:00:42.4]} 47. Bd6 {[%clk 0:01:03.3]} 47... Nd4 {[%clk 0:00:40.5]} 48. Kf1 {[%clk 0:01:02.6]} 48... e2+ {[%clk 0:00:39.2]} 0-1\n'
    assert type(get_pgn_gamelength(sample_pgn)) == float
    # This was calculated by hand, as it was a pretty short game
    assert get_pgn_gamelength(sample_pgn) == 284


def test_get_total_length():
    # Gets the archive used for testing in the first function.
    archive = get_chesscom_archive("erik", "2019", "10")
    test = get_total_length(archive)
    assert type(test) == tuple
    assert test[1] == 74
