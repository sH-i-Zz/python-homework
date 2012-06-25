import unittest
import base64, pickle
import homework

class GameOfLifeTestCase(homework.Test):
    def test_step_board(self):
        for el in BOARD_TEST_DATA:
            orig, expected = el
            board = self.decodeboard(orig)
            self.solution.step_board(board)
            self.assertTrue(self.encodeboard(board), expected)


    def decodeboard(self, n, size = 50):
        flat = bin(pickle.loads(base64.decodebytes(n)))[2:].rjust(size * size,"0")
        board = []
        for i in range(0, size):
            board.append([int(x) for x in flat[(i*size): ((i+1)*size)]])

        return board

    def encodeboard(self, board):
        flat = "".join(["".join([str(x & 1) for x in row]) for row in board])
        return base64.encodebytes(pickle.dumps(int(flat, 2)))


BOARD_TEST_DATA = [
    ( b'gAOLMgEAAAAAAAAAAACgBBBCVABIQoABAAALAACAKAAOABEIAoIACAAAAIEAAGwAAAQIgIBRQFoA\nEEBIAgQAIEARCEBQYJBoEgAACziAAAAABIAiFzAiAEBCBAAQAAARwEAVAIAIQAAAhAAQoIHBAACB\nAABAACBAAEAAAAWCAEAiKgEQIAAsAIAYEBQAAAkxAQAAxgkMAMJBREQgCBAQIgLVgQEAqggAAAIg\nCCAIgIAQgBBAIECAAgKBzAiAAE5AgCAgACACCAQAQ0UASCJkAhAKBEACgBMAZGAQwYAEABfDAjDC\nAAIFAAAHBASGIMBmASCAQAKgAQIBAAAAEQQAEEAIIBQACI0AmoBAQyBCQEkIBAIAAhMAgEBAAAQB\nAgIAAAAACgAAAAQAAAAgBEhEAhEAIABAhIABQC4=\n' , b'gAOLMQEAAAAAAAAAAACgBBBCVAAAAYAAAAAHAAAGAAAaAAAAQAAQAA4AAAABAHAAAAQAAPAiADgA\nACCKAzgAIIA7DADgYAxwAAAAAzAAAgAADKAABQAAAAACBGAIAAADIAAAAIAM4AAYAAAwgAEAAAAA\nAAAAAAAAAAAAAQCAAIAGAAAMAAAcQAA8AADAIQBxAFAAghsMAIAAlOUIAAACJgPCwQEAUBwAAgYA\nQAAAAIBAQABgMABAAAYAwAAAABgAgAJgACgAAAQAAcIBADAAxgIAGBiAECEAYGA4AMIAAALCAOCC\nAA4NBCAWAgwOAADCACAAAAAwAQAAAAAADw4AAAAAZjgAAIwB+CGAQzAAAAcADgAAgCEAAAAAAAwA\nAQAAAAAABAAAAAAAAAAAAAAAACAAMAAAAIAALg==\n' ),
    ( b'gAOLMgEAAAAAAAAAAAAEUj4JIAQhhJAAAgIlAIIAEACkAASABAgAABAxAsAAIABoBQAIUIAAAkQI\nAKEKIAAEAAARgEDQAACAIIAAAQQCAAQFAIgBDAwABACKQAIOAAAwBGgIAABBQAHAIBAAQEAOAQBA\nAAAAAgAAAgEAAYIAAsAkICACCAAATEECIAAQBAABBAEAAGwCggABQAAIEAABIAAQQAAYEAAEhgEA\nAABaQACAhACBAmAAAEAIKACAACggGAABoAFBgwIKQQgAACICBJAMAUCEAACRIIAEABIAQAQAAAQF\nAIiAAAAAwEGEBBARBBAIQQAAIhAIKASAYKIHgACCAMJCCFABICAQgDNhAJACAggAIAAQgAAAADEg\nAAAAQCAAQiAwgCJxQANEAEENFARAAQSUQYBFDC4=\n' , b'gAOLMgEAAAAAAAAAAAAEUj4JIIQQwIkAAABcAAMAAABIAAwEABAAAAA4A0AAAAAgAQAH4EABDwAA\ngEADEAA6AAAxAADAAAAAAICBAwAAAwMCAIABCAgDAAAKICwGAAAoABAIAADAIEDiAAAAAACEAwAA\nAAAwAAAAAQAAAAAABAAAIhABHAACgMAAYAAAAI0BAAAAAAAGgAAAAAAMGAAEAAAAwAAIAAAOgAFg\nAABYAAwAAADABgAAAAQMGoAAAAAwMAABAAGAgQEEAAoCABQQAGAMAMAAAAAwAAAAAAAAAAAAAAAA\nIBgAAAAIgAAGAAAAAAwABwAAKBAAEAAAwLEDQCgCAMUCQKwAAFABAKMiAAABAAgAAAAcAAAAABBA\nAAAAQKAI4AAwgGEjAANAAAMtCA4gAQAyIAAADi4=\n' ),
    ( b'gAOLMgEAAAAAAAAAAAAAAAAALABICSQABAAIXEAFAhAAIIUCAEQAMBgAhwJBALAAKAAAJAAAAQBQ\nABQwUQEAKIihCgBGBAABAIARBAADAQAAAKIQIAFUCAEIIgBQQAAAAGoAAI4ggAACAgQAAWAyQIIA\nAACxAEQAFQAAQ4QAIIQJlYAACAIAphAICAAZQAEAADAAnIOVACAAAAARAQQoRQCoACCASEAAUAEA\nIQQAAAIQWABICAAAABAyAQAAqAIAAFSAgBAAAggCAMCICAAAAAECSFAACAIBAQIUAIBZDAAABAAD\nAAAIAAgAEEQCUAAcUACCAgECAAgBAAMEBBgAEQAKAIIgBIAACRDSEgABKAiAQIAGAQAAAiIAyBJB\noIABAAgmwigAAADABqBTAKBBAoJAFmAAAFAAAi4=\n' , b'gAOLLQEAAAAAAAAAAAAAAAAALACADSAAAAAA1mABAAAA6AWDAOAAACAABwAAADAADAAIAAAEYAAA\nACBwAwCACOCABQAGAMADAAAYAAAGAAAMAAIMAAAgAAAAQA2AwAMAAECAAIcAAMgGACgAAGAgAAAA\nAoAxAQIACABABAAAYACAFQABAAAAlgAACAwAHuEAABAAiIMKAEAAEAQRAAAQAgBACACAnAAAgAAA\nNQAAAAIACAAMAAAAsAAwAAAAUADAAAAAQDkAAAAAAMAAHAAAAAADQAAACAAOAwAAAMAJDAAAAAAH\nAAAACAAICABAIAAIIAAAQAEgAAYABAIEADAAAAACAIBwDgAABADgOYADEADAwAAGMAAABGAAAIEB\nYIQBAAT+wiUOAHD4BLGhABAABwBFA0Au\n' ),
    ( b'gAOLMQEAAAAAAAAAAEARAAAJAEAAAAFAAAAAAAgQJBBABOFCEAAAACAQgEAAooAjAACAJEQAAhAC\nRgiwIAEAEAoAAFUDAkELFAAAAAAFCgCMBEARqQAARAGAAAAAAACBAaABQIGCQQAAEAgCgAAgwQAA\nlJAIIAEAkwAAsQEEAGAgCAATAEAAAQTCGAERAQENBAAAAAAKBACAQAE4CiAhIggAEAAAQEACAAAC\nhVBgKAABgAAIAQECAAAANBAAQCIAREBAAQoBACAAAlQ6BAgIRAAAYAQAAEBQAhZAQhsgBwgBAAAA\nSGCgABIAQAAAwUAQAEKEmgAIFACIAAQwBOAABABCQFIEIAABUAEEEABABSACACAAAAQDAAICIAAA\nMACgAQQgAAwAggAECRAACgKAkIIAAJAgAOBALg==\n' , b'gAOLMAEAAAAAAAAAAEARAAAJAAAAAAAAAAAAAAwAAgAAAHAAMAAAECAcAAAAAIBBAACAGAcSAAAA\nzgEAgOIAMHCAAwoAAGADAIAFAIAEKAAAAAA4QAAAAACgAAAAIADAAQAAAIAAAwAEMAAGBAAA4AAA\nCAAA/AMAIAAAwAEAACAAgAMZAECAAADDCAAAAAAPAQAAAAACAAAAAAAoDAAAAAhAEACAQCAAAAAA\nAABgAAAAAAAAAQACAAAAMggAAAEA4ACAAJsHAAAAAzgcCAAAACC44AIAoANgAS4AAACADSQAAA4A\nJGBAAAIAwIDBRAAAAAAAjAIMAAgAAQAwKOAABADCCAAAAACAgIAAAAAAgEIAAAAACAABAAAAAAAM\nAADAAQAAAAwAAgAAABAABAYAAHAAAAAAAEAu\n' ),
    ( b'gAOLLwEAAAAAAAAAAABAFQAAJMJAgQAhBIAAABCYQACMABAwJABAIQRQQAAAEAEEGQCBCAxAAEEA\nAgAOBBgRgQKAFAoIBRLQIIhpEABAKAEAACBRIBiAQkAAgESUAgAkJAAAAIAAAFCAFAAAIg4ABACA\nIAgCEoIggESDQAQCIANSAUAgIAAIAEQAKEWAhCBAokgAQoCGAgAgEEAEACABBIIGIABAGAEESAAE\nAABIBBAQAiEQAAACQQkBEExgBORBsUQCAAQAKBgEAAAAAAhIECBABAAQMIBEBDAAgAEEQBCAAQQi\nIEAYCgAADhIAUAAACEAICAAAA4gAgABAIAjACAQQkAAAQAABAAgBKpLAAEIQYQAAAICCgCgBBIAA\nQFAAAIAiQAgSAKIEALOGkQAUAEACBwQIIC4=\n' , b'gAOLMgEAAAAAAAAAAABAFQAAJAKAAgACCIAAAACQAQAMAABYAAAgAgBAAAAAggOAAACAAAwBAAIA\nQgAEAAyDAAFAEBQYBAQgdRBwCACgFAOAAQAAMBhAAYCAAGAABQAAAAggBoAAgAAAAAAAAIYADgAA\nUEgAOAAggMEPAAgEAAMLACAAwAiQAgAAWANAAPBBIAgABoACAQAAAMAPBAAABoACAAAAGAAWAAAA\nYAAIAAAgAAAAAACCgO4gGAgAAOAAcK4DAAADQB0OAAAAAAAICAAAAAAAEIABCABgQAEMACCAAQYA\nAQAACgAABwAAMAAACGAAAAAAAAAwAAAAHAAAAAAAAAEARgAgAAAADAAAAGAAIAQAAwABgBkAAEAF\nAOAAAAACQFwiAAANADMFgQAPAMAFBQAAAAAACC4=\n' ),
    ( b'gAOLMQEAAAAAAAAAAKgogQAIAAASAIBwAAEgAAAAgACEAAYiAAABQZkEAMAAACAAEAACBIAJAohB\nioAoAIAwAAxAgABBAIQAAECBAACEABAEAgBAAIgEAFgAAgAEA4IAAQACAAh0AizAAAAAAAAQQICI\nUAQ4BIQADIFBQAIUUAEqEKgEAAAACAIAmAAgQsARABAAAAEAEIIHAAKZAAAAAAFAMACoCEIAAcQA\nAAAQFAAACQJAAEAABEgIgQEABAAAQSChAUgAhAACAAABIgJAABAQQgkoAAAkAhAAAiAIEBBAEBAk\noCECBAgAkRCENAAKCgiAEAAARAAKAAQGcBAgBAYACQAAAVAAEgEglEAAEABAAFAARgBKBUACABIB\nAgMAAADAGogAAAAAhCAAAiCARAEAQChBAAIILg==\n' , b'gAOLMAEAAAAAAAAAAKgogQAIAAAVAABwAABwAACAAADAAAYAAAAAAAQAAMAAABAAAAADAMAFAAAM\nAgEsAEA4AAZAAADgAAAAAICCAQAAAAAAAAAAAIAAADgAAAAAAMALAAAwAAAgAAAAAADgCAAMAwAI\nIQA4AAADLoDhABQCEAACABAAAABQABAACAAAYIAAQOAAgAEBAIADAAAYAAACAADAAAAAAACAAQBA\nAQAACAAAAADgQAAAAgCAAAAAAAAAAgAgAAAAjAEAAAACMAcEAAAIgAwAAAAABAoAAAAYOAAAAABg\noAAADACAAQYAMAAADgAAoAAAJAAEgAAAMABwAAYAQACAAxAADgAACKAAOABgAKAAwAAAA4AAAABg\nCAMAAACAHRgAAAAAnQAAAAAAgAEAAAAAAAIu\n' ),
    ( b'gAOLMAEAAAAAAAAAAAAACGAhIEBCUILCJBCAAEQAAAAIATAAAgkAAwAhIMAAAkADgSAAQQgAEARA\nQLEDAhIAAA4BAgRgRgAgAoCFCYBIIIAABAAAQQEBoMCMAwGAIAEACUCgQAQEABI4BAEgEAAIQAAB\nAoBAQoACAQAEiAUASAEAAFAAACSAAAEI4TIACAQAAAQkAYEAABFAEAEAAEAAARYBZBFIAIkKAACJ\nIDAEBhIAQAAqLCGAABQgAAaAAAgFEAIAAQCASBiRgNgAgIoBQABHEkECAIAEICRAAACBJGQQCAyI\nECUIAABAQKBQAGAAAFARxAUABwEEAoAEAAgBSGAEAAgAEglIACAhABIABgBFACMVkAAEAREABIiI\ngEAAEGEAQA0AAEEsFEEQAKIAC5ABAAQwUjAu\n' , b'gAOLMAEAAAAAAAAAAAAACGAhIAAAIIDCAACAAAYAAQCAATAAABAAAyABEEAADAACgAEAINwAAAYA\nALABAACAAY4LAOBgBiAABAAAGgDAMAAAHgAjQQAAcACABwIAgAMDCgAEwQAAAAAQAAAAAACwIAAA\nAAAAYAAAAAAAgAkAgAAAACgAYAQAAAAAwDEAAAAAgA0AAAAAADjggAEAAAAAAA4BAAAAAIAHgAMA\nAHAbBwAAgAAMjAEAAAJQQAcAAAAAAAoAADAA4DyAAGABwLEBAGAEABcGAAAUEBYAAAADwHgAAAAI\nOGgIACgAALAgIAAAAQCDgIABAoACAJYACAQADAAIABAAgAOIAOAAwDwABoDBAAYAGAAOABAAABwA\ngAMAIHAHgg4AgMBAAFgAAALYP4QBAAAAPCAu\n' ),
    ( b'gAOLMgEAAAAAAAAAAACDIAAABgSQAEEoAAASECCAAAZIEiQEISA4IAzgxxgAAEAQwLARBEAFRBAI\nJgICQB0QCSFAAFEIBBACAAAwEIAQgACAAAI4EAABAAAIEUhAIABQAAAAIBAIBQJAAAAAAkgABGCQ\nQSYICATAAAAAAAABYVAAAAICkiAMAJABCAAAAAQgAACADAAggAgRAAAAAAQAEAGKAgBAgBQAiiAg\nAgAQAgIhEAIiEAAKsDIgCjJAEgQgDQAEQBABAAAACAAAgAEAQAAQIACIkAUQQYMAAEEEAKIAkAhQ\nEAAAAAIgEIJAAFAAAEgoAYBlSECASQOCAAACAAAAQQAmKAERCAENUEFCQQEIRSUAMQAQABgVgCAA\nAABCIFFIaQAEAIECgQACggADAACECAAAAABEIC4=\n' , b'gAOLLAEAAAAAAAAAAACDIAAABgQEAAAQAAAgAACAAAQYAAJ4Mxw4ABjg73zAANCAtLMBAAADIAQK\nIgAKIDQAGAAAAFoMBgAAAABwAAAQAADAAAJ0AAAAAAD4AAAAAADAAAAAAAAAAwAAAABgCBwAAgAw\nAAAAAIDADBAAAAAAYQAAAAAAggEAAAAACAAwAAAEAAAAAAAAgAAAIABAAAAAAAIAAAAAAAgAASAA\nAgAABAABFARAAAwO4BHQBgAAIM4AHAAAAAAAUAAAAAAAAAAAwAAAYAAAgAMAQAEAAAUIAAYAgAA4\nAAAAAAYAAAAAANAAABjwA0BjAMDAAQDGAYACAgAAAwAHOAAgiACeUANAAAAcAI0CMgAAAJgJgAAg\nAAAiAOCAcAAAAAAAwgEAgAAHAAAIHC4=\n' ),
    ( b'gAOLMwEAAAAAAAAAAAAEIlgAEIEgEAAAhIAAQAQACGAAgiQgAUAAACAQCAAAwEEgQAQCRIACoNAE\nAgIEAQCQgIJAAgABAAAgACAAACEAAEAAKIBAwgIDgACSIIgIIAARCHABaQEgAKMEAyUEAQcASRJQ\nAIRkAAAEpwElAFACSRAAqQMKADMBAC4ICAAgQIDBAUQAYwAjAAGlgAAUBABJEgoCQAgAAEAAAAAA\nAGAAQpEQAQCACCAIqIABAIAAhQQAAQABRQAgBAUUIgpAAgBGSAAAEAAAAQCQAFIggAMUDBAAECAE\nEQAMBAAgJBAAhFCEpAGRBgAgwQAAFBLi4BACAQCAAAAgQABAAgAAABAEIABQKLaQAAAAJBAANhBA\nBSoA8AEAIQiAIAECAwBUhAAAgETAIhALBCBBAgEu\n' , b'gAOLMgEAAAAAAAAAAAAEIlgAEAEAGAAAAIgA4AAAACAAABgAAIAAMDAACAAAgMAAcAgAgIMCACAM\nAgEMAIAAAAAAAAAAAAQAAAAAAAAAAEAAEMABAAEDQAAGAQIMMAAYwMDDYAFgQIMDRw0IAA0ZDAhA\nAIQAAAgABQDiQQABfAMAwAYDACMAAGtICAhAADDBAIAAYQABAYBBzAAEAAAIAQQAAAgAACgAAAAA\nAAAAAIAAAMAAAGCAUAAAAMCAQgEEAAABBgEAAAACPgAAAABAAAAAAAAYoAAAAQAAAAEgDoADAASI\nOAAAAAAwPgBwAADAqAEAD4AoyAcAFACgwAEAIADAAAEAAAAABAAAgBsAAAAAEG6AAAAgAjUAQgCA\nCAUAEAEAAxAAYAEAAgBYhAAAAABAIAAAAAAABy4=\n' ),
    ( b'gAOLMgEAAAAAAAAAAIiAgAAAIMAAFxEACAAFBCGAKCBAgInhUIAABASAJAAgGgBMQAQAEAIKLgBs\nCALCIAAQECILAEATBAgAAAQQAAbACgAVCEQaCBpACAhCCEiAAYUohQABAASAAIAIQQYAQAAAAoAg\nggKAAQAgAAACBIAAAMAFkIAAAAhAAQASAAaJgSKAAAgEMEAQABkgGICAACgAkAARAAABAAAQAQEw\nggSgBAJAkQMYEAQAQABSA6CAAABBEAIEAAABmBACAEAAgAAAAgQYgAgASAggJAAAIgCiJCgAAAAA\nGIQYABgAgAAAgEAEAAggkICACgARCAAQBlABvERAJBALAIBIAACBQAACoCQAAASKhCSkQRABACAB\nhARCoKAEIhDlABCABVEAAgRIAQAQCAAAAAEiEC4=\n' , b'gAOLLAEAAAAAAAAAAIiAgAAAIMABBQAABAAB1CIQKAAAgIPhcQAABQaFogAgHACEBgAAcAAIHgAM\nAARFYAC4AQQEAAACgABoAIAEAAIABQAoAAgYExzAABhTENCAAQIAAgADAApACAAAAAAAQABgAAAA\nAAGAAQAgADAADAAAAIAIAAABAADFQAAAAAaADQAAABgMCEAAABwAeIAAADAAYAACAAAAAAC4AAA4\ngABADgJAGAP4ARwAAATQAgAAAACAEAABAAAAcAAAAAAGIAEAAgAYAAAACAAgAAQAIABADxAAAAAA\nOEAAABgAQAAAAEAAAAAAAACAACAAGwAAG2ADeAAgGCAHUIAJEAAAAAAGQAAAAAKEAH2AAQAQEOAB\nD4I+AEAAIDDAAQGhACAIBgAAAoAADC4=\n' ),
]



if __name__ == "__main__":
    GameOfLifeTestCase.main()

