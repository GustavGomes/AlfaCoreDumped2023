using System.Runtime.CompilerServices;
using AlfaCoreDumped.Domain.Entities.CompanyResources;
using AlfaCoreDumped.Domain.Models;
using AlfaCoreDumped.Infrastructure.DbRepository;
using Microsoft.AspNetCore.Mvc;

namespace AlfaCoreDumped.Controllers
{
    [ApiController]
    [Route("area")]
    public class AreaController : ControllerBase
    {
        private IAlfaRepository _alfaRepository;
        public AreaController(IAlfaRepository alfaRepository)
        {
            _alfaRepository = alfaRepository;
        }

        [HttpGet("{areaId}")]
        public ActionResult<Area> GetArea(Guid areaId)
        {
            var area = _alfaRepository.GetArea(areaId);
            if (area == null)
            {
                return NotFound();
            }
            return Ok(area);
        }

        [HttpPost]
        public void PostArea(AreaCreationModel area)
        {
            Area newArea = new Area
            {
                Id = new Guid(),
                Code = area.Code,
                Description = area.Description,
                LiberationStatus = area.LiberationStatus,
                PdfFile = area.PdfFile
            };
            _alfaRepository.AddArea(newArea);
            _alfaRepository.Save();
        }
    }
}